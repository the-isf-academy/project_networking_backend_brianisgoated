# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Drill(Model):
    drill_name = StringField()
    instructions = StringField()
    comments = StringField()
    level = IntegerField()
    tip = StringField()
    likes = StringField

    def json_response(self):
        return {
            'comments': self.comments, 
            'drill_name': self.drill_name,
            'instructions': self.instructions,
            'level': self.level,
            'tip': self.tip
        }
    
    def change_tip(self, new_tip):
        self.tip = new_tip
        self.save()

    def change_comments(self, new_comments):
        self.comments = new_comments
        self.save()

    def add_likes(self):
        self.likes += 1
        self.save()

    
