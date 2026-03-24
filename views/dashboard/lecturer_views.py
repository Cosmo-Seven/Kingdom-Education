from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from core.models import (
  LecturerModel,
 
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required

@custom_login_required("dashboard_login")
@role_permission_required("view_lecturermodel")
def lecturer_list(request):
    try:
        lecturers = LecturerModel.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            lecturers = lecturers.filter(Q(name__icontains = search)|Q(position__icontains = search)|Q(total_students__icontains = search))

        context = {
            "lecturers":lecturers,
            "search":search
        }
        return render(request,"dashboard/lecturer_list.html", context)

    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")
    
@custom_login_required("dashboard_login")
@role_permission_required("add_lecturermodel")
def lecturer_create(request):
    try:
        if request.method == "POST":
            lecturer = LecturerModel.objects.create(
                name = request.POST.get("name"),
                featured_image = request.FILES.get("featured_image"),
                position = request.POST.get("position"),
                total_students = request.POST.get("total_students"),
                video_url = request.POST.get("video_url"),
                about = request.POST.get("about")
            )
            lecturer.save()
            messages.success(request,"lecturer Create Successfully!")
            return redirect("lecturer_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("update_lecturermodel")
def lecturer_update(request, pk):
    try:
        if request.method == "POST":
            lecturer = get_object_or_404(LecturerModel, id = pk)
            lecturer.name = request.POST.get("name")
            lecturer.position = request.POST.get("position")
            lecturer.total_students = request.POST.get("total_students")
            lecturer.about = request.POST.get("about")
            lecturer.video_url = request.POST.get("video_url")
            if request.FILES.get("featured_image"):
               if lecturer.featured_image:
                  lecturer.featured_image.delete(save=False)
               lecturer.featured_image = request.FILES.get("featured_image")
            lecturer.save()
            messages.success(request,"lecturer Update Successfully!")
            return redirect("lecturer_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("delete_lecturermodel")
def lecturer_delete(request, pk):
    try:
            lecturer = get_object_or_404(LecturerModel, id = pk)
            if lecturer.featured_image:
                lecturer.featured_image.delete()
            lecturer.delete()
            messages.success(request,"lecturer Delete Successfully!")
            return redirect("lecturer_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")


    


