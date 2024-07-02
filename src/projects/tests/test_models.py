from django.contrib.auth import get_user_model
from django.test import TestCase

from projects.models import Project

User = get_user_model()


class ProjectTests(TestCase):
    def setUp(self):
        # Create users for testing
        self.user1 = User.objects.create_user(
            email='user1@example.com',
            password='testpassword',  # noqa
        )
        self.user2 = User.objects.create_user(
            email='user2@example.com',
            password='testpassword',  # noqa
        )

        # Common data for test cases
        self.project_data = {
            'name': 'Test Project',
        }

    def test_create_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1, self.user2)
        assert Project.objects.count() == 1
        assert project.name == 'Test Project'
        assert self.user1 == project.observers.all()
        assert self.user2 == project.observers.all()

    def test_retrieve_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1, self.user2)
        retrieved_project = Project.objects.get(id=project.id)
        assert retrieved_project.name == 'Test Project'
        assert self.user1 in retrieved_project.observers.all()
        assert self.user2 in retrieved_project.observers.all()

    def test_update_project(self):
        project = Project.objects.create(**self.project_data)
        project.observers.add(self.user1)
        project.name = 'Updated Project'
        project.observers.remove(self.user1)
        project.observers.add(self.user2)
        project.save()
        updated_project = Project.objects.get(id=project.id)
        assert updated_project.name == 'Updated Project'
        assert self.user1 == updated_project.observers.all()
        assert self.user2 in updated_project.observers.all()

    def test_delete_project(self):
        project = Project.objects.create(**self.project_data)
        project_id = project.id
        project.delete()
        with self.pytest.raises(Project.DoesNotExist):
            Project.objects.get(id=project_id)
