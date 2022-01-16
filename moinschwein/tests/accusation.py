from django.test import TestCase
from django.urls import reverse

from moinschwein.models import Accusation, User, Word


__all__ = ['AccusationTestCase']


class AccusationTestCase(TestCase):

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

        cls.another_user = User.objects.create_user(
            username='another_dude',
            email='testuser@example.com',
            password='password',
        )

        cls.sample_word = Word.objects.create(bad_word='Test')

    def test_create_accusation_without_login(self):
        response = self.client.post(reverse('submit_accusation'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f'{reverse("login")}?next={reverse("submit_accusation")}')

    def test_create_accusation(self):
        self.client.login(**self.credentials)

        response = self.client.post(
            reverse('submit_accusation'),
            data={
                'offender': self.user.id,
                'snitch': self.another_user.id,
                'word': self.sample_word.id,
            },
        )
        self.assertEqual(response.status_code, 200)

        accusation = Accusation.objects.first()
        self.assertEqual(accusation.offender.id, self.user.id)

    def test_create_accusation_with_invalid_data(self):
        self.client.login(**self.credentials)

        response = self.client.post(
            reverse('submit_accusation'),
            data={
                'offender': 123,
                'snitch': 1337,
                'word': 987,
            },
        )
        self.assertEqual(response.status_code, 400)
