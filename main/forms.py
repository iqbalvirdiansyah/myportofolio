from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "role",
            "short_description",
            "full_description",
            "tech_stack",
            "link",
            "project_image_url",
        ]
        labels = {
            "title": "Nama Proyek",
            "role": "Peran Anda",
            "short_description": "Deskripsi Singkat",
            "full_description": "Deskripsi Lengkap",
            "tech_stack": "Teknologi yang Digunakan",
            "link": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Portfolio Website", "maxlength": 255}),
            "role": TextInput(attrs={"placeholder": "Frontend Developer", "maxlength": 255}),
            "short_description": TextInput(attrs={"placeholder": "Deskripsi Singkat", "maxlength": 300}),
            "full_description": Textarea(attrs={"placeholder": "Ceritakan Proyekmu secara rinci", "rows": 3}),
            "tech_stack": TextInput(attrs={"placeholder": "Django, Python, HTML, CSS"}),
            "link": URLInput(attrs={"placeholder": "https://github.com/..."}),
            "project_image_url": URLInput(attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}),
        }
