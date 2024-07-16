from django.test import TestCase
from .models import Game
from rest_framework.test import APIClient
from django.urls import reverse

# Create your tests here.

# Prueba de que crea el juego correctamente
class GameModelTest(TestCase):
    def test_create_game(self):
        game = Game.objects.create(player_x="Player1", player_o="Player2")
        self.assertEqual(game.player_x, "Player1")
        self.assertEqual(game.player_o, "Player2")
        self.assertEqual(game.board, "---------")
        self.assertEqual(game.current_turn, "X")
        self.assertIsNone(game.winner)


# Prueba de un movimiento correcto
class GameGoodMoveTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = Game.objects.create(player_x="Player1", player_o="Player2")

    def test_valid_move(self):
        response = self.client.patch(
            reverse('game-detail', kwargs={'pk': self.game.id}),
            {'position': 0, 'player': 'X'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.game.refresh_from_db()
        self.assertEqual(self.game.board[0], 'X')
        self.assertEqual(self.game.current_turn, 'O')
        self.assertIsNone(self.game.winner)
        

# Prueba si se ha intentado poner una pieza en una casilla ya ocupada o si un jugador no está en su turno
class GameInvalidMoveTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = Game.objects.create(player_x="Player1", player_o="Player2")
        self.game.board = "X--------"
        self.game.current_turn = "O"
        self.game.save()

    def test_move_on_occupied_position(self):
        response = self.client.patch(
            reverse('game-detail', kwargs={'pk': self.game.id}),
            {'position': 0, 'player': 'O'},
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_player_turn(self):
        response = self.client.patch(
            reverse('game-detail', kwargs={'pk': self.game.id}),
            {'position': 1, 'player': 'X'},
            format='json'
        )
        self.assertEqual(response.status_code, 400)
        

# Prueba de que hay un ganador       
class GameWinnerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = Game.objects.create(player_x="Player1", player_o="Player2")
        self.game.board = "XX-------"
        self.game.save()

    def test_detect_winner(self):
        response = self.client.patch(
            reverse('game-detail', kwargs={'pk': self.game.id}),
            {'position': 2, 'player': 'X'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.game.refresh_from_db()
        self.assertEqual(self.game.winner, 'X')
        

# Prueba de que hay un empare       
class GameWinnerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = Game.objects.create(player_x="Player1", player_o="Player2")
        self.game.board = "OXOOXOXO-"
        self.game.current_turn = "X"
        self.game.save()

    def test_detect_draw(self):
        response = self.client.patch(
            reverse('game-detail', kwargs={'pk': self.game.id}),
            {'position': 8, 'player': 'X'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.game.refresh_from_db()
        self.assertEqual(self.game.winner, 'D')