class Player:
  def __init__(self, name : str, position : int = 1):
    self.name = name
    self.position = position

  def get_postion(self):
    return self.position
  
  def get_name(self):
    return self.name
  
  def update_position(self, new_position):
    self.position = new_position

  

