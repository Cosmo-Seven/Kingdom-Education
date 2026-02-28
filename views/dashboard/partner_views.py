from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from core.models import (
    PartnerModel,
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required


def partner_list(request):
    try:
        partners = PartnerModel.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            partners = partners.filter(Q(title__icontains=search))
        context = {"partners": partners, "search": search}
        return render(request, "dashboard/partner_list.html", context)
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("dashboard")


def partner_create(request):
    try:
        if request.method == "POST":
            partner = PartnerModel.objects.create(
                title=request.POST.get("title"),
                logo=request.FILES.get("logo"),
                link=request.POST.get("link"),
            )
            partner.save()
            messages.success(request, "Partner Create Successfully!")
            return redirect("partner_list")
    except Exception as e:
        messages.error(request, f"Error{str(e)}")
        return redirect("dashboard")

def partner_update(request, pk):
    try:
        if request.method == "POST":
            partner = get_object_or_404(PartnerModel, id = pk)
            partner.title = request.POST.get("title")
            partner.link = request.POST.get("link")
            if request.FILES.get("logo"):
                if partner.logo:
                   partner.logo.delete(save=False)
                partner.logo = request.FILES.get("logo")
            partner.save()
            messages.success(request,"Partner Update Successfully!")
            return redirect("partner_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")
    
def partner_delete(request, pk):
    try:
            partner = get_object_or_404(PartnerModel, id = pk)
            if partner.logo:
                partner.logo.delete()
            partner.delete()
            messages.success(request,"Partner Delete Successfully!")
            return redirect("partner_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")