import datetime
from http import HTTPStatus

from django.test import TestCase

from django.urls import reverse

from inventory.models import Game


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
        with open('resources/valid_pgn.pgn') as pgn:
            pgn_string = pgn.read()

        response = self.client.post(url, {'description': "Test Form", 'pgn': pgn_string})

        self.assertRedirects(response, reverse('game', kwargs={'pk': 1}))

    def test_add_game_enriches_and_saves_game_model(self):
        url = reverse('add_game')
        with open('resources/valid_pgn.pgn') as pgn:
            pgn_string = pgn.read()
        description = "Test Form"

        self.client.post(url, {'description': description, 'pgn': pgn_string})

        game = Game.objects.get(pk=1)

        self.assertEqual(game.description, description)
        self.assertEqual(game.pgn, pgn_string)
        self.assertEqual(game.event, 'WR Chess Masters 2023')
        self.assertEqual(game.site, 'Dusseldorf GER')
        self.assertEqual(game.date, datetime.date(2023, 2, 16))
        self.assertEqual(game.round, '1')
        self.assertEqual(game.white, 'Nepomniachtchi,I')
        self.assertEqual(game.black, 'Abdusattorov,Nodirbek')
        self.assertEqual(game.result, '1/2-1/2')

    def test_get_games_returns_httpstatus_ok(self):
        url = reverse('games')

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_game_returns_httpstatus_ok(self):
        game = Game(description="Test Game", pgn="Test PGN")
        game.save()
        url = reverse('game', kwargs={'pk': game.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
