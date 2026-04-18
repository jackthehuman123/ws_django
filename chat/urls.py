from django.urls import path
from . import views

urlpatterns = [
    path("chat/<str:room_name>/history/", views.room_history, name="room_history")
]