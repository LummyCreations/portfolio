from django.urls import path
from . import views

urlpatterns = [
    path("", views.portapp_index, name="portapp_index"),
    path("<int:pk>/", views.portapp_detail, name="portapp_detail"),
]
