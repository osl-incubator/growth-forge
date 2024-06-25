# test models code yet to be inserted
# test models code yet to be inserted
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from growth_plan.models import GrowthPlanItem

User = get_user_model()


class GrowthPlanItemTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            # username='testuser',
            password='testpassword',
            email='test@test.com',
        )
        self.client.login(
            # username='testuser',
            password='testpassword',
            email='test@test.com',
        )

        # Common data for test cases
        self.growth_plan_item_data = {
            'user': self.user,
            'title': 'Test Growth Plan',
            'description': 'This is a test description.',
            'start_date': timezone.now().date(),
            'end_date': (timezone.now() + timedelta(days=10)).date(),
            'progress_percentage': 50,
        }

    def test_create_growth_plan_item(self):
        growth_plan_item = GrowthPlanItem.objects.create(
            **self.growth_plan_item_data
        )
        self.assertEqual(GrowthPlanItem.objects.count(), 1)
        self.assertEqual(growth_plan_item.title, 'Test Growth Plan')

    def test_retrieve_growth_plan_item(self):
        growth_plan_item = GrowthPlanItem.objects.create(
            **self.growth_plan_item_data
        )
        retrieved_item = GrowthPlanItem.objects.get(id=growth_plan_item.id)
        self.assertEqual(retrieved_item.title, growth_plan_item.title)

    def test_update_growth_plan_item(self):
        growth_plan_item = GrowthPlanItem.objects.create(
            **self.growth_plan_item_data
        )
        growth_plan_item.title = 'Updated Title'
        growth_plan_item.save()
        updated_item = GrowthPlanItem.objects.get(id=growth_plan_item.id)
        self.assertEqual(updated_item.title, 'Updated Title')

    def test_delete_growth_plan_item(self):
        growth_plan_item = GrowthPlanItem.objects.create(
            **self.growth_plan_item_data
        )
        growth_plan_item_id = growth_plan_item.id
        growth_plan_item.delete()
        with self.assertRaises(GrowthPlanItem.DoesNotExist):
            GrowthPlanItem.objects.get(id=growth_plan_item_id)
