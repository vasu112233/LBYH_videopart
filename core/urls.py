from django.urls import path
from .views import *

urlpatterns = [
    path("video/", videopage, name="video"),
    path("courses/", coursepage, name="coursepage"),
    path("course/<str:slug>", course, name="course"),
    path("", homepage, name="home"),
]
