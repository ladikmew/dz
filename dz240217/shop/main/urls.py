from django.urls import path

from main.views import main_view,category_view

urlpatterns = [
    path("", main_view, name="main"),
    path("category/<int:category_id>/", category_view, name="category"),
    #path("", views.index, name="index"),
]