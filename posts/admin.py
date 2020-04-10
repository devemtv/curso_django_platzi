""" Post admin class"""

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = (
        'pk',
        'title',
        'createdAt',
    )

    list_editable = (
    )

    list_display_links = (
        'pk',
        'title',
    )
