from typing import List
from snake import Snake
from ladder import Ladder
import random
class Board:
  def __init__(self, snakes_num : int = 6, ladder_num : int = 6):
    self.snakes : List[Snake]  = []
    self.ladders : List[Ladder] = []
    self._initialize_snakes(snakes_num)
    self._initialize_ladders(ladder_num)

  def _initialize_snakes(self, snakes_num : int ):
    for _ in range(snakes_num):
      self.snakes.append(Snake(Board.get_random_position(), Board.get_random_position()))

  def _initialize_ladders(self, ladders_num : int):
    for _ in range(ladders_num):
      self.ladders.append(Ladder(Board.get_random_position(), Board.get_random_position()))

  def get_random_position():
    return random.randint(2, 99)

  def check_snake_head(self, position):
    for snake in self.snakes:
      if position == snake.get_start():
        return True
      
    return False
  
  def check_ladder_start(self, position):
    for ladder in self.ladders:
      if position == ladder.get_start():
        return True
      
    return False
  
  def get_new_position_after_snake(self, position):
    for snake in self.snakes:
      if position == snake.get_start():
        return snake.get_end()
      
    return position
  
  def get_new_position_after_ladder(self, position):
    for ladder in self.ladders:
      if position == ladder.get_start():
        return ladder.get_end()

    return position
  
  def get_new_postion_after_snake_ladder(self,position : int):
    for snake in self.snakes:
      if position == snake.get_start():
        return snake.get_end()

    for ladder in self.ladders:
      if position == ladder.get_start():
        return ladder.get_end()

    return position
  
