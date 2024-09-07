from game_manager import GameManager
class Demo:
  def run():
    game_manager = GameManager.get_instance()


    players1 = ["player 1", "player 2", "player 3"]
    game_manager.start_game(players1)

    players2 = ["player 4", "player 5", "player 6"]
    game_manager.start_game(players2)

if __name__ == "__main__":
  Demo.run()
