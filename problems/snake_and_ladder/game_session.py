from typing import List
from board import Board
from dice import Dice
from player import Player

class GameSession:
  def __init__(self, player_names : List[str]):
    self.board = Board()
    self.dice = Dice()
    self.players = [Player(name) for name in player_names]
    self.current_player_turn = 0

  def play(self):
    while not self.is_game_over():
      current_player = self.players[self.current_player_turn]
      dice_roll = self.dice.roll()

      new_position = current_player.get_postion() + dice_roll

      if new_position <= 100:
        current_player.update_position(self.board.get_new_postion_after_snake_ladder(new_position))
        print(f"{current_player.get_name()} rolled a {dice_roll} and moved to position {current_player.get_postion()}")
      
      if current_player.get_postion() == 100:
        print(f"{current_player.get_name()} wins!")
        break

      self.current_player_turn = (self.current_player_turn + 1)%len(self.players)


  def is_game_over(self):
    for player in self.players:
      if player.get_postion() == 100:
        return True
    return False