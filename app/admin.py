from django.contrib import admin
from .models import Heading, Feedback, Government


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Heading model.

    This class customizes the Django admin interface for the Heading model.
    It specifies which fields are displayed in the admin list view.

    Attributes:
        list_display (list): Fields to display in the admin list view.
                             Includes 'id', 'title', 'image', and 'desc'.
    """
    list_display = ['id', 'title', 'image', 'desc']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Feedback model.

    This class customizes the Django admin interface for the Feedback model.
    It specifies which fields are displayed in the admin list view.

    Attributes:
        list_display (list): Fields to display in the admin list view.
                             Includes 'id', 'name', 'email', 'desc', and 'image'.
    """
    list_display = ['id', 'name', 'email', 'desc', 'image']


@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Government model.

    This class customizes the Django admin interface for the Government model.
    It specifies which fields are displayed in the admin list view.

    Attributes:
        list_display (list): Fields to display in the admin list view.
                             Includes 'id', 'image', 'title', 'about', and 'source'.
    """
    list_display = ['id', 'image', 'title', 'about', 'source']
    