from django.urls import reverse_lazy


def routes(request):
    return {
        # ======================================== Dashboard ========================================
        "dashboard_url": reverse_lazy("dashboard"),
        "course_create_url": reverse_lazy("course_create"),
        # ==================================== User ================================================
        "user_list_url": reverse_lazy("user_list"),
        "user_create_url": reverse_lazy("user_create"),
        # =================================== Role ==================================
        "role_list_url": reverse_lazy("role_list"),
        "role_create_url": reverse_lazy("role_create"),
        # Dashboard Login
        "dashboard_login_url": reverse_lazy("dashboard_login"),
        "dashboard_logout_url": reverse_lazy("dashboard_logout"),
        # lecture
        "lecturer_list_url": reverse_lazy("lecturer_list"),
        "lecturer_create_url": reverse_lazy("lecturer_create"),
        # Payment method
        "payment_method_list_url": reverse_lazy("payment_method_list"),
        "payment_method_create_url": reverse_lazy("payment_method_create"),
        # blog category
        "blog_category_list_url": reverse_lazy("blog_category_list"),
        "blog_category_create_url": reverse_lazy("blog_category_create"),
        # blog
        "blog_list_url": reverse_lazy("blog_list"),
        "blog_create_url": reverse_lazy("blog_create"),
        # partner
        "partner_list_url": reverse_lazy("partner_list"),
        "partner_create_url": reverse_lazy("partner_create"),
        # ========== Topic ========== #
        "course_topic_list_url": reverse_lazy("course_topic_list"),
        "course_topic_create_url": reverse_lazy("course_topic_create"),
        # ========== Contact ========== #
        "contact_list_url": reverse_lazy("contact_list"),
        # ========== Enroll =========== #
        "enroll_list_url": reverse_lazy("enroll_list"),
        # ========== Donation ========= #
        "donation_list_url":reverse_lazy("donation_list"),
        # LanguageModel
        "language_list_url": reverse_lazy("language_list"),
        "language_create_url": reverse_lazy("language_create"),
        # Text Key And Translate
        "translation_list_url": reverse_lazy("translation_list"),
        "text_key_create_url": reverse_lazy("text_key_create"),
        # Volunteer 
        "volunteer_list_url":reverse_lazy("volunteer_list"),
        "volunteer_create_url":reverse_lazy("volunteer_create"),
        # ======================================== Website ========================================
        "home_url": reverse_lazy("home"),
        "courses_url": reverse_lazy("courses"),
        "blogs_url": reverse_lazy("blogs"),
        "student_profile_url": reverse_lazy("student_profile"),
        "lecturer_profile_url": reverse_lazy("lecturer_profile"),
        "contact_us_url": reverse_lazy("contact_us"),
        "login_url": reverse_lazy("login"),
        "register_url": reverse_lazy("register"),
        "logout_url": reverse_lazy("logout"),
        "course_topics_url": reverse_lazy("course_topics"),
        "course_details_url": reverse_lazy("course_details"),
        "partners_url": reverse_lazy("partners"),
        "donation_form_url":reverse_lazy("donation_form"),
        "form_upload_url":reverse_lazy("form_upload"),
        
    }
