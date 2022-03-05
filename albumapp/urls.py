from django.urls import path
from . import views
urlpatterns = [
    path('sam',views.hai, name="demo" ),
    path("add", views.addphotos, name = "add"),
    path('', views.gallary, name = "gal"),
    path("see", views.viewphoto, name = "open"),
]