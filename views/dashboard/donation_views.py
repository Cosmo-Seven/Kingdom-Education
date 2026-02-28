from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from core.models import (
    DonationModel,
    ProgramModel
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required

def donation_list(request):

    donations = DonationModel.objects.all().order_by("-created_at")
    search = request.GET.get("search")
    if search:
            donations = donations.filter(Q(name__icontains = search) | Q(email__icontains = search )| Q(phone__icontains = search))
    context = {
        "donations":donations,
        "search":search
    
    }
    return render(request,"dashboard/donation_list.html",context)

def donation_delete(request,pk):
      donation = get_object_or_404(DonationModel, id = pk)
      donation.delete()
      messages.success(request,"Donation Delete Successfully!")
      return redirect("donation_list")
