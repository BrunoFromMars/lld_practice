from commentable import Commentable
from votable import Votable
from vote import Vote
from tag import Tag

class Question(Commentable, Votable):
    def __init__(self, title, text, author, tag_names) :
        self.id = id(self)
        self.title = title
        self.text = text
        self.tags = [Tag(name) for name in tag_names]
        self.votes = []
        self.author = author
        self.answers = []
        self.comments = []

    def add_comment(self, comment):
        return self.comments.append(comment)
    
    def get_comments(self):
        return self.comments.copy()

    def add_answer(self, answer):
        self.answers.append(answer)
    
    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Vote must be either 1 or -1")
        self.votes = [ v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 5)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    
