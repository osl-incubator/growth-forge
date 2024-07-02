# test models code yet to be inserted
from django.contrib.auth import get_user_model
from django.test import TestCase
from djf_surveys.models import Survey

from one_on_one.models import Link

User = get_user_model()


class LinkTests(TestCase):
    def setUp(self):
        # Create users for testing
        self.mentor = User.objects.create_user(
            email='mentor@example.com',
            password='testpassword',  # noqa
        )
        self.mentee = User.objects.create_user(
            email='mentee@example.com',
            password='testpassword',  # noqa
        )

        # Create surveys for testing
        self.mentor_survey = Survey.objects.create(name='Mentor Survey')
        self.mentee_survey = Survey.objects.create(name='Mentee Survey')

        # Common data for test cases
        self.link_data = {
            'mentor': self.mentor,
            'mentee': self.mentee,
            'mentor_survey': self.mentor_survey,
            'mentee_survey': self.mentee_survey,
            'periodicity': 'weekly',
            'times': 5,
        }

    def test_create_link(self):
        link = Link.objects.create(**self.link_data)
        assert Link.objects.count() == 1
        assert link.mentor.email == 'mentor@example.com'
        assert link.mentee.email == 'mentee@example.com'
        assert link.periodicity == 'weekly'

    def test_retrieve_link(self):
        link = Link.objects.create(**self.link_data)
        retrieved_link = Link.objects.get(id=link.id)
        assert retrieved_link.mentor.email == 'mentor@example.com'
        assert retrieved_link.mentee.email == 'mentee@example.com'

    def test_update_link(self):
        link = Link.objects.create(**self.link_data)
        link.periodicity = 'monthly'
        link.times = 10
        link.save()
        updated_link = Link.objects.get(id=link.id)
        assert updated_link.periodicity == 'monthly'
        assert updated_link.times == 10  # noqa

    def test_delete_link(self):
        link = Link.objects.create(**self.link_data)
        link_id = link.id
        link.delete()
        with self.pytest.raises(Link.DoesNotExist):
            Link.objects.get(id=link_id)
