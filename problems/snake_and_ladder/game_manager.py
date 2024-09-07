import threading
from typing import List
from game_session import GameSession

class GameManager:
  _instance = None
  _lock = threading.Lock()

  def __init__(self):
    self.games = []

  @staticmethod
  def get_instance():
    if not GameManager._instance:
      with GameManager._lock:
        if not GameManager._instance:
          GameManager._instance = GameManager()
    return GameManager._instance
  
  def start_game(self, player_names : List[str]):
    game = GameSession(player_names)
    self.games.append(game)
    threading.Thread(target=game.play).start()