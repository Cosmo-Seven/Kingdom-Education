from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from core.models import (
    EnrollModel,
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required
from enums.enroll import EnrollStatusEnum


def enroll_list(request):
    enrolls = EnrollModel.objects.all().order_by("-created_at")
    search = request.GET.get("search")
    if search:
        enrolls = enrolls.filter(Q(student__email__icontains = search) | Q(course__title__icontains = search) | Q(payment_method__name__icontains = search))
    else:
        search = None
    context = {
        "enrolls":enrolls,
        "search":search,
        "status":EnrollStatusEnum.choices
    }
    return render(request,"dashboard/enroll_list.html", context)

def status_change(request, pk):
    try:
        enroll = get_object_or_404(EnrollModel, id = pk)
        if request.method == "POST":
            enroll.status = request.POST.get("status")
            enroll.save()
            messages.success(request,"Status Change Successfully!")
            return redirect("enroll_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("course_topic_list")
