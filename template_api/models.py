from ast import mod
from email.policy import default
from random import choices
from unicodedata import category
from django.db import models
from mongoengine import *
class questions(models.Model, ):
    QUESTION_TYPE = [
    ('QQ', 'Quick Question'),
    ('Q', 'Question')
    ]

    category = StringField(max_length=2, choices=QUESTION_TYPE)
    question = StringField(max_length=1000, required=True)
    answer = ListField(StringField(max_length=2000), default=[], required=True)
    next_question = ReferenceField()
