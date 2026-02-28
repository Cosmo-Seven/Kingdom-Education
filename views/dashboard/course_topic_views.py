from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from core.models import (
    CourseTopicModel,
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required


@custom_login_required("dashboard_login")
@role_permission_required("view_coursetopicmodel")
def course_topic_list(request):
    course_topics = CourseTopicModel.objects.all()
    search = request.GET.get("search")
    if search:
        course_topics = course_topics.filter(Q(name__icontains = search))
    context = {
        "topics": course_topics,
    }
    return render(request, "dashboard/course_topic_list.html", context)


@custom_login_required("dashboard_login")
@role_permission_required("add_coursetopicmodel")
def course_topic_create(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")
            featured_image = request.FILES.get("featured_image")
            course_topic = CourseTopicModel.objects.create(
                name = name,
                description = description,
                featured_image = featured_image
            )
            course_topic.save()
            messages.success(request, "Course Topic Created.")
            return redirect("course_topic_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("course_topic_list")

@custom_login_required("dashboard_login")
@role_permission_required("change_coursetopicmodel")
def course_topic_update(request, pk):
    try:
        course_topic = get_object_or_404(CourseTopicModel, id=pk)
        if request.method == "POST":
            course_topic.name = request.POST.get("name")
            if request.FILES.get("featured_image"):
                if course_topic.featured_image:
                    course_topic.featured_image.delete(save=False)
                course_topic.featured_image = request.FILES.get("featured_image")
            course_topic.description = request.POST.get("description")
            course_topic.save()
            messages.success(request, "Course Topic Updated.")
            return redirect("course_topic_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("course_topic_list")

@custom_login_required("dashboard_login")
@role_permission_required("delete_coursetopicmodel")
def course_topic_delete(request, pk):
    try:
        course_topic = get_object_or_404(CourseTopicModel, id=pk)
        course_topic.delete()
        messages.success(request, "Course Topic Deleted.")
        return redirect("course_topic_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("course_topic_list")