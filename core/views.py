from django.shortcuts import render
from .models import *

# Create your views here.


def homepage(request):
    return render(request, "index.html")


def coursepage(request):
    courses = Course.objects.all()
    return render(request, "courses/index.html", {"courses": courses})


def course(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get("lecture")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number=serial_number, course=course)
    context = {"course": course, "video": video}
    return render(request, "courses/page.html", context=context)


def videopage(request):
    videos = Video.objects.all()
    return render(request, "videos/index.html", {"videos": videos})
