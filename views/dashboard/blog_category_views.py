from django.shortcuts import redirect,render,get_object_or_404
from core.models import (
    BlogCategoryModel,
)
from django.contrib import messages
from django.db.models import Q
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required

@custom_login_required("dashboard_login")
@role_permission_required("view_blogcategorymodel")
def blog_category_list(request):
    try:
        blog_categories = BlogCategoryModel.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            blog_categories = blog_categories.filter(Q(name__icontains = search))
        context = {
            "blog_categories":blog_categories,
            "search":search
        }
        return render(request,"dashboard/blog_category_list.html", context)
    except Exception as e:
        messages.error(request,f"Error: {str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("add_blogcategorymodel")
def blog_category_create(request):
    try:
        if request.method == "POST":
            blog_category = BlogCategoryModel.objects.create(
                name = request.POST.get("name"),
            )
            blog_category.save()
            messages.success(request,"Blog Category Create Successfully!")
            return redirect("blog_category_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")
    
@custom_login_required("dashboard_login")
@role_permission_required("change_blogcategorymodel")
def blog_category_update(request, pk):
    try:
        if request.method == "POST":
          blog_category = get_object_or_404(BlogCategoryModel, id = pk)
          blog_category.name = request.POST.get("name")
          blog_category.save()
          messages.success(request,"Blog Category Update Successfully!")
          return redirect("blog_category_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("delete_blogcategorymodel")
def blog_category_delete(request, pk):
    try:
            blog_category = get_object_or_404(BlogCategoryModel, id = pk)
            blog_category.delete()
            messages.success(request,"Blog Category Delete Successfully!")
            return redirect("blog_category_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")