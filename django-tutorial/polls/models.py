from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # pregunta
    pub_date = models.DateTimeField('date published') # fecha de publicacion

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # pregunta asociada
    choice_text = models.CharField(max_length=200) # texto de la opcion
    votes = models.IntegerField(default=0) # votos de la opcion