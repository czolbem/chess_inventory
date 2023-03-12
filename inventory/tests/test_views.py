from http import HTTPStatus

from django.test import TestCase

from django.urls import reverse

from inventory.models import Game


class ViewTests(TestCase):
    def test_get_home_returns_200(self):
        url = reverse('home')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_add_game_returns_200(self):
        url = reverse('add_game')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_games_returns_200(self):
        url = reverse('games')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_game_returns_200(self):
        game = Game(description="Test Game", pgn="Test PGN")
        game.save()
        url = reverse('game', kwargs={'pk': game.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
