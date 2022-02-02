import json

from django.test import TestCase
from django.urls import reverse

from moinschwein.models import User, Accusation, Word


__all__ = ['DashboardTestCase']


class DashboardTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'username': 'test_user',
            'password': '12345678',
        }

        cls.user = User.objects.create_superuser(
            **cls.credentials,
            email='testuser@example.com',
            first_name='Unit',
            last_name='Test',
        )

        cls.sample_word = Word.objects.create(bad_word='Test')

    def test_get_live_accusations_without_login(self):
        response = self.client.get(reverse('live_accusations'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f'{reverse("login")}?next={reverse("live_accusations")}')

    def test_get_live_accusations(self):
        self.client.login(**self.credentials)

        sample_accusation = Accusation.objects.create(
            offender=self.user,
            snitch=self.user,
            word=self.sample_word,
        )
        response = self.client.get(reverse('live_accusations'))
        content, *_ = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(sample_accusation.timestamp.strftime('%H:%M:%S'), content)

    def test_accusation_counter_without_accusations(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context_data.get('accusations_against_self_percentage'), 0.0)

    def test_accusation_counter_with_accusation(self):
        self.client.login(**self.credentials)

        Accusation.objects.create(
            offender=self.user,
            snitch=self.user,
            word=self.sample_word,
        )

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context_data.get('accusations_against_self_percentage'), 100.0)
