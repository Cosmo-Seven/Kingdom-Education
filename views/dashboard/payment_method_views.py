from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from core.models import (
    PaymentMethodModel,
    )
from django.contrib import messages
from utils.decorators import custom_login_required
from decorators.role_decorators import role_permission_required


@custom_login_required("dashboard_login")
@role_permission_required("view_paymentmethodmodel")
def payment_method_list(request):
    try:
        payments = PaymentMethodModel.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            payments = payments.filter(Q(name__icontains = search)|Q(number__icontains = search))
        context = {
            "payments":payments,
            "search":search
        }
        return render(request,"dashboard/payment_method_list.html", context)
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("add_paymentmethodmodel")
def payment_method_create(request):
    try:
        if request.method == "POST":
          payment = PaymentMethodModel.objects.create(
              name = request.POST.get("name"),
              number = request.POST.get("number"),
              featured_image = request.FILES.get("featured_image")
          )
          payment.save()
          messages.success(request,"Payment Method Create Successfully!")
          return redirect("payment_method_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("update_paymentmethodmodel")
def payment_method_update(request, pk):
    try:
        if request.method == "POST":
          payment = get_object_or_404(PaymentMethodModel, id = pk)
          payment.name = request.POST.get("name")
          payment.number = request.POST.get("number")
          if request.FILES.get("featured_image"):
              if payment.featured_image:
                  payment.featured_image.delete()
              payment.featured_image = request.FILES.get("featured_image")
          payment.save()
          messages.success(request,"Payment Method Update Successfully!")
          return redirect("payment_method_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("delete_paymentmethodmodel")
def payment_method_delete(request, pk):
    try:
            payment = get_object_or_404(PaymentMethodModel, id = pk)
            if payment.featured_image:
                payment.featured_image.delete()
            payment.delete()
            messages.success(request,"Payment method  Delete Successfully!")
            return redirect("payment_method_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")