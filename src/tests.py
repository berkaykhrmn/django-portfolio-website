from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project, About, Skill, Contact, Homepage

class ModelsTestCase(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(
            title = "Test Project",
            content = "This is a test project",
            link = "http://127.0.0.1:8000/",
        )
        self.assertEqual(project.title, "Test Project")
        self.assertTrue(project.id is not None)

    def test_skill_creation(self):
        about = About.objects.create(title = "Test About", content = "This is a test")
        skill = Skill.objects.create(about = about, name = "Test Skill")
        self.assertEqual(skill.name, "Test Skill")


class ViewsAndFormsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.about = About.objects.create(title = "Test About", content = "This is a test")
        Skill.objects.create(about = self.about, name = "Test Skill")
        Project.objects.create(title="Test Project", content = "This is a test project", link = "http://127.0.0.1:8000/")
        Homepage.objects.create(title="Test Homepage", content = "This is a test homepage")

    def test_index_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Skill')

    def test_contact_form_submission(self):
        data = {
            'fullName': "Test Full Name",
            'email': "test@example.com",
            'message': "This is a test message"
        }
        response = self.client.post(reverse('index'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.full_name, 'Test Full Name')


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'password123')
        self.client.login(username='admin', password='password123')

    def test_admin_can_access_project(self):
        response = self.client.get('/admin/src/project/')
        self.assertEqual(response.status_code, 200)
