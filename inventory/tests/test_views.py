from http import HTTPStatus

from django.test import TestCase

from django.urls import reverse


class ViewTests(TestCase):
    def test_get_home_returns_200(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
