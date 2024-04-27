from django.contrib import admin

from .models import Category, Good

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ["name"]

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ["category","name","price"]

# admin.site.register(Post, PostAdmin)