from django.shortcuts import render
from main.models import Experience, Project

def show_main(request):
    context = {
        "name": "Iqbal Virdiansyah",
        "npm": "2206000000",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems undergraduate at Universitas Indonesia with a strong focus "
            "on Software Engineering, Artificial Intelligence, and Business Development. "
            "Passionate about integrating Data Science and Financial Management principles "
            "to architect scalable software solutions that drive organizational growth and system efficiency."
        ),
        "experience_list": Experience.objects.all(),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Iqbal Virdiansyah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Iqbal Virdiansyah",
        "projects_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)

from django.shortcuts import get_object_or_404

def show_project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "name": "Iqbal Virdiansyah",
        "project": project,
    }
    return render(request, "project_detail.html", context)
