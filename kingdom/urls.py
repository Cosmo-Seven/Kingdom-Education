from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from views.dashboard import page_views as dashboard_views
from views.dashboard import (
    payment_method_views,
    course_topic_views,
    contact_views,
    lecturer_views,
    blog_category_views,
    blog_views,
    auth_views,
    partner_views,
    enroll_views,
    donation_views,
    user_views,
    role_views,
    language_views,
    text_key_views,
    volunteer_views,
)
from views.website import page_views as website_views
from views.website import auth_views as website_auth_views

urlpatterns = (
    [
        path(settings.ADMIN_LOGIN_URL, admin.site.urls),
        # ================================================================================================
        # DASHBOARD URL
        # ================================================================================================
        path("dashboard/", dashboard_views.index, name="dashboard"),
        path(
            settings.DASHBOARD_LOGIN_URL,
            auth_views.dashboard_login,
            name="dashboard_login",
        ),
        path(
            settings.DASHBOARD_LOGOUT_URL,
            auth_views.dashboard_logout,
            name="dashboard_logout",
        ),
        path(
            "dashboard/course-form/", dashboard_views.course_form, name="course_create"
        ),
        path(
            "dashboard/course-form/<uuid:id>/",
            dashboard_views.course_form,
            name="course_update",
        ),
        path(
            "dashboard/course-form/delete/<uuid:pk>",
            dashboard_views.course_delete,
            name="course_delete",
        ),
        # User
        path("dashboard/user/list/", user_views.user_list, name="user_list"),
        path("dashboard/user/create/", user_views.user_create, name="user_create"),
        path(
            "dashboard/user/update/<uuid:pk>/",
            user_views.user_update,
            name="user_update",
        ),
        path(
            "dashboard/user/delete/<uuid:pk>/",
            user_views.user_delete,
            name="user_delete",
        ),
        # Role
        path("dashboard/role/list/", role_views.role_list, name="role_list"),
        path("dashboard/role/create/", role_views.role_create, name="role_create"),
        path(
            "dashboard/role/update/<uuid:pk>/",
            role_views.role_update,
            name="role_update",
        ),
        path(
            "dashboard/role/delete/<uuid:pk>/",
            role_views.role_delete,
            name="role_delete",
        ),
        #  lecturer
        path(
            "dashboard/lecturer/list/",
            lecturer_views.lecturer_list,
            name="lecturer_list",
        ),
        path(
            "dashboard/lecturer/create/",
            lecturer_views.lecturer_create,
            name="lecturer_create",
        ),
        path(
            "dashboard/lecturer/update/<uuid:pk>/",
            lecturer_views.lecturer_update,
            name="lecturer_update",
        ),
        path(
            "dashboard/lecturer/delete/<uuid:pk>/",
            lecturer_views.lecturer_delete,
            name="lecturer_delete",
        ),
        # Payment Method
        path(
            "dashboard/payment-method/list/",
            payment_method_views.payment_method_list,
            name="payment_method_list",
        ),
        path(
            "dashboard/payment-method/create/",
            payment_method_views.payment_method_create,
            name="payment_method_create",
        ),
        path(
            "dashboard/payment-method/update/<uuid:pk>/",
            payment_method_views.payment_method_update,
            name="payment_method_update",
        ),
        path(
            "dashboard/payment-method/delete/<uuid:pk>/",
            payment_method_views.payment_method_delete,
            name="payment_method_delete",
        ),
        # Blog Category
        path(
            "dashboard/blog-category/list/",
            blog_category_views.blog_category_list,
            name="blog_category_list",
        ),
        path(
            "dashboard/blog-category/create/",
            blog_category_views.blog_category_create,
            name="blog_category_create",
        ),
        path(
            "dashboard/blog-category/update/<uuid:pk>/",
            blog_category_views.blog_category_update,
            name="blog_category_update",
        ),
        path(
            "dashboard/blog-category/delete/<uuid:pk>/",
            blog_category_views.blog_category_delete,
            name="blog_category_delete",
        ),
        # Blog
        path("dashboard/blog/list/", blog_views.blog_list, name="blog_list"),
        path("dashboard/blog/create/", blog_views.blog_create, name="blog_create"),
        path(
            "dashboard/blog/update/<uuid:pk>/",
            blog_views.blog_update,
            name="blog_update",
        ),
        path(
            "dashboard/blog/delete/<uuid:pk>/",
            blog_views.blog_delete,
            name="blog_delete",
        ),
        # ========== Topic ========== #
        path(
            "dashboard/course-topic/list/",
            course_topic_views.course_topic_list,
            name="course_topic_list",
        ),
        path(
            "dashboard/course-topic/create/",
            course_topic_views.course_topic_create,
            name="course_topic_create",
        ),
        path(
            "dashboard/course-topic/update/<uuid:pk>/",
            course_topic_views.course_topic_update,
            name="course_topic_update",
        ),
        path(
            "dashboard/course-topic/delete/<uuid:pk>/",
            course_topic_views.course_topic_delete,
            name="course_topic_delete",
        ),
        path(
            "dashboard/partner/list/", partner_views.partner_list, name="partner_list"
        ),
        path(
            "dashboard/partner/create/",
            partner_views.partner_create,
            name="partner_create",
        ),
        path(
            "dashboard/partner/update/<uuid:pk>/",
            partner_views.partner_update,
            name="partner_update",
        ),
        path(
            "dashboard/partner/delete/<uuid:pk>/",
            partner_views.partner_delete,
            name="partner_delete",
        ),
        # ========== Contact Us ========== #
        path(
            "dashboard/contact_list/", contact_views.contact_list, name="contact_list"
        ),
        path(
            "dashboard/contact_delete/<uuid:pk>/",
            contact_views.contact_delete,
            name="contact_delete",
        ),
        # ============== Donation ============= #
        path(
            "dashboard/donation/list/",
            donation_views.donation_list,
            name="donation_list",
        ),
        path(
            "dashboard/donation/delete/<uuid:pk>/",
            donation_views.donation_delete,
            name="donation_delete",
        ),
        # ============== Language ===================== #
        path(
            "dashboard/language/list/",
            language_views.language_list,
            name="language_list",
        ),
        path(
            "dashboard/language/create/",
            language_views.language_create,
            name="language_create",
        ),
        path(
            "dashboard/language/update/<uuid:pk>/",
            language_views.language_update,
            name="language_update",
        ),
        path(
            "dashboard/language/delete/<uuid:pk>/",
            language_views.language_delete,
            name="language_delete",
        ),
        # ========================= Text Key ========================== #
        path(
            "dashboard/translation/list/",
            text_key_views.translation_list,
            name="translation_list",
        ),
        path(
            "dashboard/translations/save/",
            text_key_views.save_translation,
            name="save_translation",
        ),
        path(
            "dashboard/text_key/create/",
            text_key_views.text_key_create,
            name="text_key_create",
        ),
        path(
            "dashboard/text_key/update/<uuid:pk>/",
            text_key_views.text_key_update,
            name="text_key_update",
        ),
        path(
            "dashboard/text_key/delete/<uuid:pk>/",
            text_key_views.text_key_delete,
            name="text_key_delete",
        ),
        # =========================== Enroll =======================#
        path("dashboard/enroll/list/", enroll_views.enroll_list, name="enroll_list"),
        path(
            "dashboard/enroll/status/<uuid:pk>/",
            enroll_views.status_change,
            name="status_change",
        ),
        # =========================== Volunteer ====================
        path(
            "dashboard/volunteer/list/",
            volunteer_views.volunteer_list,
            name="volunteer_list",
        ),
        path(
            "dashboard/volunteer/create/",
            volunteer_views.volunteer_create,
            name="volunteer_create",
        ),
        path(
            "dashboard/volunteer/update/<uuid:pk>/",
            volunteer_views.volunteer_update,
            name="volunteer_update",
        ),
        path(
            "dashboard/volunteer/delete/<uuid:pk>/",
            volunteer_views.volunteer_delete,
            name="volunteer_delete",
        ),
        # ================================================================================================
        # WEBSITE URL
        # ================================================================================================
        path("set-language/", website_views.set_language, name="set_language"),
        path("", website_views.index, name="home"),
        path("privacy-policy/", website_views.privacy_policy, name="privacy_policy"),
        path("coming-soon/", website_views.coming_soon, name="coming_soon"),
        path("courses/", website_views.courses, name="courses"),
        path("course-topics/", website_views.course_topics, name="course_topics"),
        path("course-details/", website_views.course_details, name="course_details"),
        path("course-lessons/", website_views.course_lessons, name="course_lessons"),
        path(
            "lecturer-profile/",
            website_views.lecturer_profile,
            name="lecturer_profile",
        ),
        path("student-profile/", website_views.student_profile, name="student_profile"),
        path("edit-profile/", website_views.edit_profile, name="edit_profile"),
        path("blogs/", website_views.blogs, name="blogs"),
        path("partners/", website_views.partner, name="partners"),
        path(
            "blog-details/<uuid:pk>/", website_views.blog_details, name="blog_details"
        ),
        path("contact-us/", website_views.contact_us, name="contact_us"),
        path("login/", website_auth_views.login_view, name="login"),
        path("register/", website_auth_views.register_view, name="register"),
        path("logout/", website_auth_views.logout_view, name="logout"),
        path("course-topics/", website_views.course_topics, name="course_topics"),
        path("course-details/", website_views.course_details, name="course_details"),
        path(
            "enroll-course/<uuid:course_id>/",
            website_views.enroll_course,
            name="enroll_course",
        ),
        path("donation/form/", website_views.donation_form, name="donation_form"),
        path("donation/form/upload/", website_views.form_upload, name="form_upload"),
        path("about/", website_views.about, name="about"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + [re_path(r"^.*$", website_views.page_not_found, name="page_not_found")]
)
