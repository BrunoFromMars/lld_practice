class Comment:
    def __init__(self, text, user):
        self.id = id(self)
        self.text = text
        self.user = user