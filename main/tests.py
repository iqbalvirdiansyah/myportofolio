from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_projects")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="experience-search-form"')
        self.assertContains(response, reverse("main:get_experience_json"))

        json_response = self.client.get(reverse("main:get_experience_json"))
        self.assertEqual(json_response.status_code, 200)
        data = json_response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["description"], self.experience.description)
        self.assertTrue(data[0]["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")
        json_response = self.client.get(reverse("main:get_experience_json"))
        self.assertEqual(json_response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)
        json_response = self.client.get(reverse("main:get_experience_json"))
        self.assertFalse(json_response.json()[0]["fields"]["is_ongoing"])

    def test_projects_page_accessible(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")

    def test_projects_page_empty_state(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))
        self.assertContains(response, "Belum ada proyek yang ditambahkan atau ditemukan.")

    def test_projects_data_displayed(self):
        p = Project.objects.create(
            title="Test Project",
            role="Developer",
            short_description="Short desc",
            full_description="Long desc",
        )
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("api:project-list"))

        api_response = self.client.get(reverse("api:project-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data[0]["title"], "Test Project")
        self.assertEqual(api_response.data[0]["role"], "Developer")
        self.assertEqual(api_response.data[0]["short_description"], "Short desc")

        # Test Detail page
        response_detail = self.client.get(reverse("main:show_project_detail", args=[p.id]))
        self.assertEqual(response_detail.status_code, 200)
        self.assertTemplateUsed(response_detail, "project_detail.html")
        self.assertContains(response_detail, "Long desc")
