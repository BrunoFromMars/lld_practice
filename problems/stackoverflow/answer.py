from commentable import Commentable
from votable import Votable
from vote import Vote
class Answer(Commentable, Votable):
    def __init__(self, text, author, question ):
        self.id = id(self)
        self.text = text
        self.author = author
        self.question = question
        self.is_accepted  = False
        self.comments = []
        self.votes = []


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
        self.author.update_reputation(value * 10)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)
    
    def accept(self):
        if self.is_accepted:
            raise ValueError("This answer is already accepted")
        self.is_accepted = True
        self.author.update_reputation(15)
    
