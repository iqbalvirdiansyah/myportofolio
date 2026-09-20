from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        "name": "Iqbal Virdiansyah",
        "npm": "2506656816",
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

def get_experience_json(request):
    experiences = Experience.objects.all().order_by("-started_at")
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json", json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]
    context = {
        "name": "Iqbal Virdiansyah",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Iqbal Virdiansyah",
        "form": form,
        "form_title": "Tambah Pengalaman",
        "submit_label": "Simpan Pengalaman",
        "cancel_url": "main:show_experience",
    }
    return render(request, "experience_form.html", context)


def update_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Iqbal Virdiansyah",
        "form": form,
        "form_title": "Edit Pengalaman",
        "submit_label": "Perbarui Pengalaman",
        "cancel_url": "main:show_experience",
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def api_experience_detail(request, id):
    """Handle GET, PUT, DELETE for a single Experience via JSON API.
    - GET  : returns serialized Experience JSON.
    - PUT  : expects JSON body with same fields as ExperienceForm, updates the instance.
    - DELETE: deletes the instance.
    CSRF token is exempted for simplicity in this demo (in production use proper protection).
    """
    experience = get_object_or_404(Experience, id=id)
    if request.method == "GET":
        data = serializers.serialize("json", [experience])
        return JsonResponse(json.loads(data)[0], safe=False)
    elif request.method == "PUT":
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        form = ExperienceForm(payload, instance=experience)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "updated"})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    elif request.method == "DELETE":
        experience.delete()
        return JsonResponse({"status": "deleted"})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json", json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Iqbal Virdiansyah",
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)


def show_project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "name": "Iqbal Virdiansyah",
        "project": project,
    }
    return render(request, "project_detail.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    
    context = {
        "name": "Iqbal Virdiansyah",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")
