from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Projects, ProjectsAdmin)
