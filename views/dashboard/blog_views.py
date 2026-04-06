from django.shortcuts import render,redirect,get_object_or_404
from core.models import BlogModel,BlogCategoryModel
from django.contrib import messages
from django.db.models import Q
from decorators.role_decorators import role_permission_required
from utils.decorators import custom_login_required



@custom_login_required("dashboard_login")
@role_permission_required("view_blogmodel")
def blog_list(request):
    try:
        blogs = BlogModel.objects.all().order_by("-created_at")
        blog_categories = BlogCategoryModel.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            blogs = blogs.filter(Q(title__icontains = search) | Q(category__name__icontains = search))
        context = {
            "blogs":blogs,
            "blog_categories":blog_categories,
            "search":search
        }
        return render(request,"dashboard/blog_list.html", context)
    except Exception as e:
        messages.error(request,f"Error: {str(e)}")
        return redirect("dashboard")
    
@custom_login_required("dashboard_login")
@role_permission_required("add_blogmodel")
def blog_create(request):
    try:
        if request.method == "POST":
            blog = BlogModel.objects.create(
                created_by = request.user,
                title = request.POST.get("title"),
                set_title = request.POST.get("set_title"),
                category_id = request.POST.get("category"),
                featured_image = request.FILES.get("featured_image"),
                description = request.POST.get("description"),
                link = request.POST.get("link"),
                is_popular = "is_popular" in request.POST
            )
            blog.save()
            messages.success(request,"Blog Create Successfully!")
            return redirect("blog_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("update_blogmodel")
def blog_update(request, pk):
    try:
        if request.method == "POST":
            blog = get_object_or_404(BlogModel, id = pk)
            blog.title = request.POST.get("title")
            blog.set_title = request.POST.get("set_title")
            blog.category_id = request.POST.get("category")
            blog.description = request.POST.get("description")
            blog.link = request.POST.get("link")
            blog.is_popular = "is_popular" in request.POST
            if request.FILES.get("featured_image"):
                if blog.featured_image:
                   blog.featured_image.delete(save=False)
                blog.featured_image = request.FILES.get("featured_image")
            blog.save()
            messages.success(request,"Blog Update Successfully!")
            return redirect("blog_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")

@custom_login_required("dashboard_login")
@role_permission_required("delete_blogmodel")
def blog_delete(request, pk):
    try:
            blog = get_object_or_404(BlogModel, id = pk)
            if blog.featured_image:
                blog.featured_image.delete()
            blog.delete()
            messages.success(request,"Blog Delete Successfully!")
            return redirect("blog_list")
    except Exception as e:
        messages.error(request,f"Error{str(e)}")
        return redirect("dashboard")
