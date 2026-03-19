from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib import messages
from core.models import VolunteerModel
from django.db.models import Q


def volunteer_list(request):
    volunteers = VolunteerModel.objects.all().order_by("-created_at")
    search = request.GET.get("search")
    if search:
        volunteers = volunteers.filter(
            Q(name__icontains=search)
            | Q(position__icontains=search)
            | Q(department__icontains=search)
        )
    context = {"volunteers": volunteers}
    return render(request, "dashboard/volunteer_list.html", context)


def volunteer_create(request):
    try:
        if request.method == "POST":
            volunteer = VolunteerModel.objects.create(
                name=request.POST.get("name"),
                position=request.POST.get("position"),
                department=request.POST.get("department"),
                image=request.FILES.get("image"),
                about=request.POST.get("about"),
                email = request.POST.get("email"),
                phone = request.POST.get("phone")
            )
            volunteer.save()
            messages.success(request, "Volunteer Create Successfully!")
            return redirect("volunteer_list")
    except Exception as e:
        messages.error(request, f"Error{str(e)}")
        return redirect("volunteer_list")


def volunteer_update(request, pk):
    try:
        if request.method == "POST":
            volunteer = get_object_or_404(VolunteerModel, id=pk)
            volunteer.name = request.POST.get("name")
            volunteer.position = request.POST.get("position")
            volunteer.department = request.POST.get("department")
            volunteer.about = request.POST.get("about")
            volunteer.email = request.POST.get("email")
            volunteer.phone = request.POST.get("phone")
            if request.FILES.get("image"):
                if volunteer.image:
                    volunteer.image.delete()
                volunteer.image = request.FILES.get("image")
            volunteer.save()
            messages.success(request, "Volunteer Update Successfully!")
            return redirect("volunteer_list")
    except Exception as e:
        messages.error(request, f"Error{str(e)}")
        return redirect("volunteer_list")


def volunteer_delete(request, pk):
    try:
        volunteer = get_object_or_404(VolunteerModel, id=pk)
        if volunteer.image:
            volunteer.image.delete()
        volunteer.delete()
        messages.success(request, "Volunteer Delete Successfully!")
        return redirect("volunteer_list")
    except Exception as e:
        messages.error(request, f"Error{str(e)}")
        return redirect("volunteer_list")
