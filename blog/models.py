from django.db import models

class Question(model.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntergerField(default=0)