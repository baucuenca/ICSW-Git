from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # pregunta
    pub_date = models.DateTimeField('date published') # fecha de publicacion

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # pregunta asociada
    choice_text = models.CharField(max_length=200) # texto de la opcion
    votes = models.IntegerField(default=0) # votos de la opcion

    def __str__(self):
        return self.choice_text