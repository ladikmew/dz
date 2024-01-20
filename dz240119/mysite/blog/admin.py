from django.contrib import admin

<<<<<<< HEAD
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "datetime"
    list_display = ["datetime", "title"]

# admin.site.register(Post, PostAdmin)
=======
# Register your models here.
>>>>>>> 591582992b91df85190d8a066deaadf44176e86c
