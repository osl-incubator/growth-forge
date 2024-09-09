from django.contrib.auth import get_user_model
from django.test import TestCase
from projects.models import Project

from growth_forge.models import Profile

User = get_user_model()


class ProfileTests(TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(
            password='testpassword2',  # noqa
            email='test@test.com',
        )
        cls.user2 = User.objects.create_user(
            email='testuser2@example.com',
            password='testpassword',  # noqa
        )

    @classmethod
    def tearDownClass(cls):
        # Create a user for testing
        cls.user.delete()

        cls.user2.delete()

    def test_create_profile(self):
        """
        The Profile
        should be created automatically
        due to the post_save signal
        """
        profile = Profile.objects.get(user=self.user)
        assert profile is not None
        assert profile.user.email == 'test@test.com'

    def test_retrieve_profile(self):
        profile = Profile.objects.get(user=self.user)
        retrieved_profile = Profile.objects.get(id=profile.id)
        assert retrieved_profile.user.email == 'test@test.com'

    def test_update_profile(self):
        profile, _ = Profile.objects.get_or_create(user=self.user)
        # Create a Project instance and add it to the profile's projects
        project = Project.objects.create(name='Test Project')
        profile.projects.add(project)
        # Verify the profile has the project added
        assert project in profile.projects.all()

    def test_delete_profile(self):
        profile = Profile.objects.get(user=self.user)
        profile_id = profile.id
        profile.delete()

        # Check that the profile does not exist
        profile_exists = Profile.objects.filter(id=profile_id).exists()
        assert not profile_exists, "Profile still exists after deletion"
