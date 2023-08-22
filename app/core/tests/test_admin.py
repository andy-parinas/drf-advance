"""
Test for Admin modifications
"""

from django.test import  TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTest(TestCase):
    """ Test for Django Admin """

    def setUp(self) -> None:
        """ Create user and client """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password='test1234'
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='password123'
        )


    def test_users_list(self):
        """ Test users are listed on page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)