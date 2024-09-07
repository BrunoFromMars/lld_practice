from typing import Dict, List
from user import User
from question import Question
from answer import Answer
from tag import Tag
from commentable import Commentable
class StackOverflow:
    def __init__(self):
        self.users: Dict[int , User] = {}
        self.questions: Dict[int, Question] = {}
        self.answers: Dict[int, Answer] = {}
        self.tags: Dict[str, Tag] = {}
        
    
    def create_user(self, username, email):
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user
    
    def ask_question(self, user : User, title : str, text : str, tags : List[str]):
        question = user.ask_question(title, text, tags )
        self.questions[question.id] = question

        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question
    
    def answer_question(self, user : User, question, content):
        answer  = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer
    
    def add_comment(self, user : User, commentable : Commentable, content):
        return user.comment_on(commentable, content)
    
    def vote_question(self, user : User, question : Question, value):
        question.vote(user, value)

    def vote_answer(self, user : User, answer : Answer, value):
        answer.vote(user, value)

    def accept_answer(self, answer : Answer):
        answer.accept()

    