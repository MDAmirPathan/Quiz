from email.policy import default
from django.db import models
from .user_info import UserData



class QuizeQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length = 254, null=False, blank=False, unique=True)
    op1 = models.CharField(max_length = 100, default=None, null=False, blank=False)
    op2 = models.CharField(max_length = 100, default=None, null=False, blank=False)
    op3 = models.CharField(max_length = 100, default=None, null=False, blank=False)
    op4 = models.CharField(max_length = 100, default=None, null=False, blank=False)
    ans = models.CharField(max_length = 100, default=None, null=False, blank=False)


    def __str__(self) -> str:
        return self.question
    
    def addQuestion(self) -> None:
        self.save()
    

class LeaderBoard(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(UserData, on_delete=models.CASCADE, default=None)
    score = models.CharField(max_length=4, default=0, null=False, blank=False)

    def __str__(self) -> str:
        return self.player.first_name
    
    def updateBoard(self) -> None:
        self.save()