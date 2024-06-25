from django.test import TestCase
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class ProjectTests(TestCase):

    def setUp(self):
        # Create users for testing
        self.user1 = User.objects.create_user(email='user1@example.com', password='testpassword')
        self.user2 = User.objects.create_user(email='user2@example.com', password='testpassword')

        # Common data for test cases
        self.project_data = {
            'name': 'Test Project',
        }

    def test_create_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1, self.user2)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(project.name, 'Test Project')
        self.assertIn(self.user1, project.observers.all())
        self.assertIn(self.user2, project.observers.all())

    def test_retrieve_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1, self.user2)
        retrieved_project = Project.objects.get(id=project.id)
        self.assertEqual(retrieved_project.name, 'Test Project')
        self.assertIn(self.user1, retrieved_project.observers.all())
        self.assertIn(self.user2, retrieved_project.observers.all())

    def test_update_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1)
        project.name = 'Updated Project'
        project.observers.remove(self.user1)
        project.observers.add(self.user2)
        project.save()
        updated_project = Project.objects.get(id=project.id)
        self.assertEqual(updated_project.name, 'Updated Project')
        self.assertNotIn(self.user1, updated_project.observers.all())
        self.assertIn(self.user2, updated_project.observers.all())

    def test_delete_project(self):
        project = Project.objects.create(**self.project_data)
        project_id = project.id
        project.delete()
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=project_id)