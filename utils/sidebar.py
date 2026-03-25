def sidebar(request):
    return {
        "SIDEBAR_MENU": [
            {
                "title": "course management",
                "permissions": ["view_coursemodel"],
                "items": [
                    {
                        "label": "Course",
                        "url_name": "dashboard",
                        "icon": "ti ti-smart-home",
                    },
                    {
                        "label": "Topic",
                        "url_name": "course_topic_list",
                        "icon": "ti ti-badge",
                        "permission": "view_coursetopicmodel",
                    },
                ],
            },
            {
                "title": "Donation",
                "permissions": ["view_dontionmodel"],
                "items": [
                    {
                        "label": "Donation",
                        "url_name": "donation_list",
                        "icon": "ti ti-school",
                        "permission": "view_donationmodel",
                    }
                ],
            },
            {
                "title": "lecturer",
                "permissions": ["view_lecturermodel"],
                "items": [
                    {
                        "label": "Lecturer",
                        "url_name": "lecturer_list",
                        "icon": "ti ti-school",
                        "permission": "view_lecturermodel",
                    }
                ],
            },
            {
                "title": "volunteer",
                "permissions": ["view_volunteermodel"],
                "items": [
                    {
                        "label": "Volunteer",
                        "url_name": "volunteer_list",
                        "icon": "ti ti-empathize",
                        "permission": "view_volunteermodel",
                    }
                ],
            },
            {
                "title": "payment method",
                "permissions": ["view_paymentmethodmodel"],
                "items": [
                    {
                        "label": "Payment Method",
                        "url_name": "payment_method_list",
                        "icon": "ti ti-calendar-dollar",
                        "permission": "view_paymentmethodmodel",
                    }
                ],
            },
            {
                "title": "enrollments",
                "permissions": ["view_enrollmodel"],
                "items": [
                    {
                        "label": "Enrollment",
                        "url_name": "enroll_list",
                        "icon": "ti ti-file-dollar",
                        "permission": "view_enrollmodel",
                    }
                ],
            },
            {
                "title": "blog",
                "permissions": [
                    "view_blogcategorymodel",
                    "view_blogmodel",
                ],
                "items": [
                    {
                        "label": "Category",
                        "url_name": "blog_category_list",
                        "icon": "ti ti-category",
                        "permission": "view_blogcategorymodel",
                    },
                    {
                        "label": "Blog",
                        "url_name": "blog_list",
                        "icon": "ti ti-article",
                        "permission": "view_blogmodel",
                    },
                ],
            },
            {
                "title": "partner",
                "permissions": ["view_partnermodel"],
                "items": [
                    {
                        "label": "Partner",
                        "url_name": "partner_list",
                        "icon": "ti ti-heart-handshake",
                        "permission": "view_partnermodel",
                    }
                ],
            },
            {
                "title": "message",
                "permissions": ["view_contactmodel"],
                "items": [
                    {
                        "label": "Message",
                        "url_name": "contact_list",
                        "icon": "ti ti-mail",
                        "permission": "view_contactmodel",
                    }
                ],
            },
            {
                "title": "site_settings",
                "permissions": [
                    "view_languagemodel",
                    "view_translationmodel",
                    "view_sitemodel",
                    "view_hometextmodel",
                ],
                "items": [
                    {
                        "label": "languages",
                        "url_name": "language_list",
                        "icon": "ti ti-language",
                        "permissions": "view_languagemodel",
                    },
                    {
                        "label": "translations",
                        "url_name": "translation_list",
                        "icon": "ti ti-speakerphone",
                        "permissions": "view_translationmodel",
                    },
                    {
                        "label": "site_settings",
                        "url_name": "site_settings",
                        "icon": "ti ti-settings",
                        "permission": "view_sitemodel",
                    },
                    {
                        "label": "home_text",
                        "url_name": "home_text",
                        "icon": "ti ti-book",
                        "permission": "view_hometextmodel",
                    },
                ],
            },
            {
                "title": "authentication",
                "permissions": [
                    "view_rolemodel",
                    "view_usermodel",
                ],
                "items": [
                    {
                        "label": "user",
                        "url_name": "user_list",
                        "icon": "ti ti-user-cog",
                        "permission": "view_usermodel",
                    },
                    {
                        "label": "role_and_permission",
                        "url_name": "role_list",
                        "icon": "ti ti-shield-check",
                        "permission": "view_rolemodel",
                    },
                ],
            },
        ]
    }
