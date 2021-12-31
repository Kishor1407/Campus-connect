from django.contrib import admin

from .models import Blogpost, Blog_image


class PostImageAdmin(admin.StackedInline):
    model = Blog_image


@admin.register(Blogpost)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Blogpost


@admin.register(Blog_image)
class PostImageAdmin(admin.ModelAdmin):
    pass