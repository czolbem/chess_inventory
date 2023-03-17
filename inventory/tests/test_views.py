from http import HTTPStatus

from django.test import TestCase

from django.urls import reverse

from inventory.models import Game


VALID_PGN_FILE = 'resources/valid_pgn.pgn'


class ViewTests(TestCase):

    def test_get_home_returns_httpstatus_ok(self):
        url = reverse('home')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_add_game_returns_httpstatus_ok(self):
        url = reverse('add_game')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_game_redirects_to_detail_view_of_added_game(self):
        url = reverse('add_game')
        with open(VALID_PGN_FILE) as pgn:
            pgn_string = pgn.read()

        response = self.client.post(url, {'description': "Test Form", 'pgn': pgn_string})

        self.assertRedirects(response, reverse('game', kwargs={'pk': 1}))

    def test_add_game_saves_game_model(self):
        url = reverse('add_game')
        with open(VALID_PGN_FILE) as pgn:
            pgn_string = pgn.read()
        description = "Test Form"

        self.client.post(url, {'description': description, 'pgn': pgn_string})

        self.assertIsNotNone(Game.objects.get(pk=1))

    def test_get_games_returns_httpstatus_ok(self):
        url = reverse('games')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_game_returns_httpstatus_ok(self):
        with open(VALID_PGN_FILE) as pgn:
            pgn_string = pgn.read()
        game = Game(description="Test Game", pgn=pgn_string)
        game.save()
        url = reverse('game', kwargs={'pk': game.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_api_game_list_returns_httpstatus_ok(self):
        url = reverse('game-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_api_game_detail_returns_httpstatus_ok(self):
        with open(VALID_PGN_FILE) as pgn:
            pgn_string = pgn.read()
        game = Game(description="Test Game", pgn=pgn_string)
        game.save()
        url = reverse('game-detail', kwargs={'pk': game.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
