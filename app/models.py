# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Drill(Model):
    drill_name = StringField()
    instructions = StringField()
    comments = StringField()
    