from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        position = int(request.data.get('position'))
        if instance.winner:
            return Response({'detail': 'La partida ya está acabada.'}, status=status.HTTP_400_BAD_REQUEST)
        if instance.board[position] != '-':
            return Response({'detail': 'Movimiento imposible, la casilla ya está ocupada.'}, status=status.HTTP_400_BAD_REQUEST)
        if instance.current_turn != request.data.get('player'):
            return Response({'detail': 'No es tu turno.'}, status=status.HTTP_400_BAD_REQUEST)
        if position > 8 or position < 0:
            return Response({'detail': 'Casilla inválida, introduce una posición entre 0 y 8.'}, status=status.HTTP_400_BAD_REQUEST)

        board_list = list(instance.board)
        board_list[position] = instance.current_turn
        instance.board = ''.join(board_list)

        winner = self.check_winner(instance.board)
        if winner:
            instance.winner = winner
        else:
            instance.current_turn = 'O' if instance.current_turn == 'X' else 'X'
        
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def check_winner(self, board):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontales
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
            (0, 4, 8), (2, 4, 6)  # Diagonales
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != '-':
                return board[combo[0]]
        if '-' not in board:
            return 'D'  # Draw
        return None
