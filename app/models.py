# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Drill(Model):
    drill_name = StringField()
    instructions = StringField()
    comments = StringField()
    difficulty = IntegerField()
    tip = StringField()
    likes = IntegerField()

    def json_response(self):
        return {
            'comments': self.comments, 
            'drill_name': self.drill_name,
            'instructions': self.instructions,
            'difficulty': self.difficulty,
            'tip': self.tip,
            'likes': self.likes
        }
    
    def change_tip(self, new_tip):
        self.tip = new_tip
        self.save()

    def user_comments(self, new_comments):
        self.comments = new_comments
        self.save()

    def add_likes(self):
        self.likes += 1
        self.save()

    def set_difficulty(self):
        self.difficulty
    
