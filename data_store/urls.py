from django.contrib import admin
from django.urls import path
from . import views
app_name = "data_store"

urlpatterns = [
    path("about/", views.about, name="about_app"),
    path("<int:id>/", views.data_detail, name="data_detail"),
    path("all_data/", views.all_data, name="all_data"),
]
