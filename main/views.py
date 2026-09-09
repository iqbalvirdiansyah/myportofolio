from django.shortcuts import render
from main.models import Experience

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
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Iqbal Virdiansyah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
