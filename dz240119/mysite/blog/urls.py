from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),

=======
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:post_id>/", views.detail, name="detail")
>>>>>>> 591582992b91df85190d8a066deaadf44176e86c
]