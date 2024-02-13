from django.contrib import admin
from .models import Video, Course, Tag, Prerequisite, Learning

# Register your models here.


class TagAdmin(admin.TabularInline):
    model = Tag


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class LearningAdmin(admin.TabularInline):
    model = Learning


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]


admin.site.register(Video)
admin.site.register(Course, CourseAdmin)
