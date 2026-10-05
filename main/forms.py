from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Project, Experience

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title
        
    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data.get("tech_stack", "")).strip()
        
    def clean_short_description(self):
        return strip_tags(self.cleaned_data.get("short_description", "")).strip()
        
    def clean_full_description(self):
        return strip_tags(self.cleaned_data.get("full_description", "")).strip()
        
    def clean_role(self):
        return strip_tags(self.cleaned_data.get("role", "")).strip()


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]
        labels = {
            "title": "Judul / Posisi",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail (opsional)",
            "ended_at": "Tanggal Selesai (kosongkan jika masih berlangsung)",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Software Engineer Intern @ Google", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pengalaman ini secara singkat...", "rows": 4}),
            "category": Select(),
            "thumbnail": URLInput(attrs={"placeholder": "https://upload.wikimedia.org/..."}),
            "ended_at": DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make ended_at not required (blank = ongoing)
        self.fields["ended_at"].required = False
        self.fields["thumbnail"].required = False
        if self.instance and self.instance.ended_at:
            self.initial["ended_at"] = self.instance.ended_at.strftime("%Y-%m-%dT%H:%M")

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama pengalaman tidak boleh hanya berisi tag HTML.")
        return title
        
    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", "")).strip()
        
    def clean_category(self):
        return strip_tags(self.cleaned_data.get("category", "")).strip()
