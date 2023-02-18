from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    description=models.CharField(max_length=260)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description

    @property
    def question_answers(self):
        return Answers.objects.filter(questions=self)

class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name="answer")

    @property
    def upvote_count(self):
        return self.upvote.all().count()