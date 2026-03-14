from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from core.models import (
    CourseModel,
    EnrollModel,
    CourseTopicModel,
    PaymentMethodModel,
    ContactModel,
    BlogModel,
    BlogCategoryModel,
    LecturerModel,
    PartnerModel,
    ProgramModel,
    DonationModel,
    VolunteerModel,
)

from enums.donation import StatusEnum


def set_language(request):
    language = request.GET.get("language")
    request.session["language"] = language
    return redirect(request.META.get("HTTP_REFERER", "/"))


def index(request):
    popular_courses = CourseModel.objects.all()
    blogs = BlogModel.objects.all()
    context = {
        "popular_courses": popular_courses,
        "blogs": blogs,
    }
    return render(request, "website/index.html", context)


def privacy_policy(request):
    return render(request, "website/privacy_policy.html")


def coming_soon(request):
    return render(request, "website/coming_soon.html")


def courses(request):
    topic = request.GET.get("topic")
    sort = request.GET.get("sort", "newest")
    page_number = request.GET.get("page")
    search = request.GET.get("search")

    courses = CourseModel.objects.all()

    if topic:
        courses = courses.filter(topic__slug=topic)
        course = courses.first()
    else:
        course = "All Courses"

    if search:
        courses = courses.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    if sort == "newest":
        courses = courses.order_by("-created_at")
    elif sort == "oldest":
        courses = courses.order_by("created_at")
    elif sort == "price_low":
        courses = courses.order_by("regular_price")
    elif sort == "price_high":
        courses = courses.order_by("-regular_price")
    elif sort == "free":
        courses = courses.filter(regular_price=0)
    elif sort == "paid":
        courses = courses.filter(regular_price__gt=0)

    paginator = Paginator(courses, 5)
    page_obj = paginator.get_page(page_number)

    popular_courses = CourseModel.objects.filter(is_popular=True)[:5]

    context = {
        "courses": page_obj,
        "course": course,
        "popular_courses": popular_courses,
        "paginator": paginator,
        "page_number": page_obj.number,
        "page_range": paginator.get_elided_page_range(
            number=page_obj.number, on_each_side=2, on_ends=1
        ),
        "selected_sort": sort,
        "search": search,
    }
    return render(request, "website/courses.html", context)


def course_topics(request):
    topics = CourseTopicModel.objects.all()
    courses = CourseModel.objects.all()

    context = {"topics": topics, "courses": courses}

    return render(request, "website/course_topics.html", context)


def course_details(request):
    title = request.GET.get("title")
    course = None
    enroll = None
    is_locked = True
    if title:
        course = CourseModel.objects.filter(slug=title).first()
        if request.user.is_authenticated:
            enroll = EnrollModel.objects.filter(
                student=request.user, course=course, status="approved"
            ).first()

        if course and course.regular_price > 0:
            if enroll:
                is_locked = False
            else:
                is_locked = True
        else:
            is_locked = False

    context = {"course": course, "enroll": enroll, "is_locked": is_locked}
    return render(request, "website/course_details.html", context)


def course_lessons(request):
    return render(request, "website/course_lessons.html")


def lecturer_profile(request):
    profile_name = request.GET.get("name")

    if profile_name:
        profile = LecturerModel.objects.filter(slug=profile_name).first()
        courses = profile.courses.all()
    else:
        profile_name = None
        courses = None

    context = {"profile": profile, "courses": courses}
    return render(request, "website/lecturer_profile.html", context)


def student_profile(request):
    enroll_courses = EnrollModel.objects.filter(student=request.user).order_by(
        "-created_at"
    )
    context = {"enroll_courses": enroll_courses}
    return render(request, "website/student_profile.html", context)


def edit_profile(request):
    return render(request, "website/edit_profile.html")


def blogs(request):
    blog_categories = BlogCategoryModel.objects.all().order_by("-created_at")
    recent_blogs = BlogModel.objects.all()[:2]
    blogs = BlogModel.objects.all().order_by("-created_at")
    category_id = request.GET.get("category")
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    context = {
        "blog_categories": blog_categories,
        "blogs": blogs,
        "recent_blogs": recent_blogs,
        "category_id": category_id,
    }
    return render(request, "website/blogs.html", context)


def blog_details(request, pk):
    blog_categories = BlogCategoryModel.objects.all().order_by("-created_at")
    recent_blogs = BlogModel.objects.all()[:2]

    blog = get_object_or_404(BlogModel, id=pk)

    blogs = BlogModel.objects.all()
    category_id = request.GET.get("category")

    if category_id:
        blogs = blogs.filter(category_id=category_id)

    context = {
        "blog": blog,
        "blog_categories": blog_categories,
        "recent_blogs": recent_blogs,
        "blogs": blogs,
        "category_id": category_id,
    }

    return render(request, "website/blog_details.html", context)


def page_not_found(request):
    return render(request, "website/page_not_found.html")


def contact_us(request):
    if request.method == "POST":
        contact = ContactModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        contact.save()
        messages.success(request, "Message Sent Successfully")
        return redirect("contact_us")
    return render(request, "website/contact_us.html")


def enroll_course(request, course_id):
    course = get_object_or_404(CourseModel, id=course_id)
    payment_methods = PaymentMethodModel.objects.all().order_by("-created_at")
    context = {"course": course, "payment_methods": payment_methods}
    if request.method == "GET":
        if not request.user.is_authenticated:
            messages.error(request, "Please login first.")
            return redirect("login")
        return render(
            request,
            "website/enroll_course.html",
            context,
        )

    if request.method == "POST":
        enrollment = EnrollModel.objects.filter(
            student=request.user, course=course
        ).first()

        if enrollment:
            if enrollment.has_access():
                messages.info(request, "You are already enrolled.")
            else:
                messages.error(request, "Your access has expired.")
            url = reverse("course_details") + f"?title={course.slug}"
            return redirect(url)

        enrollment = EnrollModel.objects.create(
            student=request.user,
            course=course,
            message=request.POST.get("message", ""),
            payment_method_id=request.POST.get("payment"),
            screenshot=request.FILES.get("screenshot"),
        )

        enrollment.set_access_expiry()

        course.enrollment_count += 1
        course.save(update_fields=["enrollment_count"])

        messages.success(request, "Successfully enrolled!")
        url = reverse("course_details") + f"?title={course.slug}"
        return redirect(url)


def partner(request):
    partners = PartnerModel.objects.all().order_by("-created_at")
    partner_id = request.GET.get("id")
    if partner_id:
        partner_details = get_object_or_404(PartnerModel, id=partner_id)
    else:
        partner_details = None
    context = {"partners": partners, "partner_details": partner_details}
    return render(request, "website/partner.html", context)


def donation_form(request):
    programs = ProgramModel.objects.all()
    context = {
        "programs": programs,
        "status": StatusEnum.choices,
    }
    return render(request, "website/donation.html", context)


def form_upload(request):
    if request.method == "POST":
        donation = DonationModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            status=request.POST.get("status"),
            amount=request.POST.get("amount") or 0,
            payment=request.POST.get("payment"),
        )
        program_ids = request.POST.getlist("programs")
        donation.program.set(program_ids)
        messages.success(request, "Donation Form Create Successfully!")
        return redirect("donation_form")


def about(request):
    page = request.GET.get("page")
    volunteers = VolunteerModel.objects.all().order_by("-created_at")
    context = {"page": page, "volunteers": volunteers}
    return render(request, "website/about.html", context)
