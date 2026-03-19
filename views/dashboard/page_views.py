from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from utils.decorators import custom_login_required
from decorators.role_decorators import role_permission_required
from core.models import (
    LecturerModel,
    CourseModel,
    CourseTopicModel,
    SectionModel,
    LessonModel,
    FileModel,
    ContactModel,
)
from django.contrib import messages


@custom_login_required("dashboard_login")
@role_permission_required("view_coursemodel")
def index(request):
    courses = CourseModel.objects.all()
    context = {"courses": courses}
    return render(request, "dashboard/index.html", context)


@custom_login_required("dashboard_login")
@role_permission_required("add_coursemodel")
def course_form(request, id=None):
    context = {
        "lecturers": LecturerModel.objects.all(),
        "topics": CourseTopicModel.objects.all(),
        "level_choices": CourseModel.LEVEL_CHOICES,
    }

    course = None
    if id:
        course = CourseModel.objects.get(id=id)
        sections = SectionModel.objects.filter(course=course)
        context["course"] = course
        context["sections"] = sections

    # ======================
    # COURSE CREATE / UPDATE
    # ======================
    if "course_submit" in request.POST:

        title = request.POST.get("title")
        description = request.POST.get("description")
        topic_id = request.POST.get("topic")
        level = request.POST.get("level")
        regular_price = request.POST.get("regular_price")
        enrollment_count = request.POST.get("enrollment_count")
        sale_price = request.POST.get("sale_price")
        learning_outcomes = request.POST.get("learning_outcomes")
        requirements = request.POST.get("requirements")
        access_duration_days = request.POST.get("access_duration_days")
        is_popular = True if request.POST.get("is_popular") else False

        topic = CourseTopicModel.objects.get(id=topic_id) if topic_id else None

        # ======================
        # CREATE
        # ======================
        if not course:

            course = CourseModel.objects.create(
                title=title,
                description=description,
                topic=topic,
                level=level,
                regular_price=regular_price,
                sale_price=sale_price or None,
                learning_outcomes=learning_outcomes,
                requirements=requirements,
                access_duration_days=access_duration_days or None,
                is_popular=is_popular,
                enrollment_count=enrollment_count,
                featured_image=request.FILES.get("featured_image"),
            )

            # lecturers
            lecturers = request.POST.getlist("lecturers")
            course.lecturers.set(lecturers)

            messages.success(request, "Course created successfully")
            return redirect("course_update", course.id)

        # ======================
        # UPDATE
        # ======================
        else:

            course.title = title
            course.description = description
            course.topic = topic
            course.level = level
            course.regular_price = regular_price
            course.sale_price = sale_price or None
            course.learning_outcomes = learning_outcomes
            course.requirements = requirements
            course.access_duration_days = access_duration_days or None
            course.is_popular = is_popular
            course.enrollment_count = enrollment_count

            if request.FILES.get("featured_image"):
                if course.featured_image:
                    course.featured_image.delete()
                course.featured_image = request.FILES.get("featured_image")

            course.save()

            lecturers = request.POST.getlist("lecturers")
            course.lecturers.set(lecturers)

            messages.success(request, "Course updated successfully")
            return redirect("course_update", course.id)

    # ======================
    # SECTION CREATE
    # ======================
    if "create_section_submit" in request.POST:
        section = SectionModel.objects.create(
            title=request.POST.get("section_title"),
            description=request.POST.get("section_description"),
            course=course,
        )
        messages.success(request, f"Section '{section.title}' created successfully")
        return redirect("course_update", course.id)

    # ======================
    # SECTION UPDATE
    # ======================
    if "update_section_submit" in request.POST:
        section = SectionModel.objects.get(id=request.POST.get("section_id"))
        section.title = request.POST.get("section_title")
        section.description = request.POST.get("section_description")
        section.save()
        messages.success(request, "Section updated successfully")
        return redirect("course_update", course.id)

    # ======================
    # SECTION DELETE
    # ======================
    if "delete_section_submit" in request.POST:
        section = SectionModel.objects.get(id=request.POST.get("section_id"))
        section.delete()
        messages.success(request, "Section deleted successfully")
        return redirect("course_update", course.id)

    # ======================
    # LESSON CREATE
    # ======================
    if "create_lesson_submit" in request.POST:
        lesson = LessonModel.objects.create(
            title=request.POST.get("lesson_title"),
            description=request.POST.get("lesson_description"),
            section_id=request.POST.get("section_id"),
            video_url=request.POST.get("video_url"),
        )
        messages.success(request, f"Lesson '{lesson.title}' created successfully")
        return redirect("course_update", course.id)

    # ======================
    # LESSON UPDATE
    # ======================
    if "update_lesson_submit" in request.POST:
        lesson = LessonModel.objects.get(id=request.POST.get("lesson_id"))
        lesson.title = request.POST.get("lesson_title")
        lesson.description = request.POST.get("lesson_description")
        lesson.video_url = request.POST.get("video_url")
        lesson.save()
        messages.success(request, "Lesson updated successfully")
        return redirect("course_update", course.id)

    # ======================
    # LESSON DELETE
    # ======================
    if "delete_lesson_submit" in request.POST:
        lesson = LessonModel.objects.get(id=request.POST.get("lesson_id"))
        lesson.delete()
        messages.success(request, "Lesson deleted successfully")
        return redirect("course_update", course.id)

    # ======================
    # FILE CREATE
    # ======================
    if "create_file_submit" in request.POST:
        file = FileModel.objects.create(
            title=request.POST.get("file_title"),
            description=request.POST.get("file_description"),
            lesson_id=request.POST.get("lesson_id"),
            file=request.FILES.get("file"),
        )
        messages.success(request, f"File '{file.title}' created successfully")
        return redirect("course_update", course.id)

    # ======================
    # FILE UPDATE
    # ======================
    if "update_file_submit" in request.POST:
        file = FileModel.objects.get(id=request.POST.get("file_id"))
        file.title = request.POST.get("file_title")
        file.description = request.POST.get("file_description")

        if request.FILES.get("file"):
            if file.file:
                file.file.delete()
            file.file = request.FILES.get("file")

        file.save()
        messages.success(request, "File updated successfully")
        return redirect("course_update", course.id)

    # ======================
    # FILE DELETE
    # ======================
    if "delete_file_submit" in request.POST:
        file = FileModel.objects.get(id=request.POST.get("file_id"))
        if file.file:
            file.file.delete()
        file.delete()
        messages.success(request, "File deleted successfully")
        return redirect("course_update", course.id)

    return render(request, "dashboard/course_form.html", context)
