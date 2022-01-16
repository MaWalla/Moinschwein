from django.test import TestCase
from django.urls import reverse

from moinschwein.models import User


__all__ = ['AuthTestCase']


class AuthTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'username': 'test_user',
            'password': '12345678',
        }

        cls.user = User.objects.create_superuser(
            **cls.credentials,
            email='testuser@example.com',
        )

    def test_login(self):
        response = self.client.post(reverse('login'), data=self.credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('dashboard'))

    def test_logout(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))
