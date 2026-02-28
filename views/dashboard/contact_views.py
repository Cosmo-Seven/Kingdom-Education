from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from core.models import (
    ContactModel
)
from django.contrib import messages
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required


@custom_login_required("dashboard_login")
@role_permission_required("view_contactmodel")
def contact_list(request):
    contacts = ContactModel.objects.all().order_by('-created_at')
    search = request.GET.get("search")
    if search:
        contacts = contacts.filter(Q(name__icontains = search)|Q(subject__icontains = search))
    return render(request, "dashboard/contact_us.html", {"contacts":contacts})


@custom_login_required("dashboard_login")
@role_permission_required("delete_contactmodel")
def contact_delete(request, pk):
    try:
        contact = get_object_or_404(ContactModel, id=pk)
        contact.delete()
        messages.success(request, "Message Deleted.")
        return redirect("contact_list")
    except Exception as e:
        messages.error(request, f"Error : {str(e)}")
        return redirect("contact_list")