from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Company, UserProfile
from complaints.models import Complaint
from django.urls import reverse

class ComplaintSubmissionTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Bank",
            industry="BANK"
        )

        self.user = User.objects.create_user(
            username="consumer1",
            password="testpass123"
        )

        UserProfile.objects.create(
            user=self.user,
            company=self.company,
            role="CONSUMER"
        )

        self.client.login(
            username="consumer1",
            password="testpass123"
        )

    def test_consumer_can_submit_complaint(self):
        response = self.client.post(
            reverse("create_complaint"),
            {
                "title": "Test Complaint",
                "description": "Something went wrong",
                "category": "Service"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Complaint.objects.count(), 1)
