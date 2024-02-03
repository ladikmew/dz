from django.contrib import admin

from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "datetime"
    list_display = ["datetime", "username","text"]

# admin.site.register(Post, PostAdmin)