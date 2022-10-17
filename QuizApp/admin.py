from django.contrib import admin
from .models import QuizeQuestions, UserData, LeaderBoard
# Register your models here.


class AdminUserData(admin.ModelAdmin):
    list_display = ['id', 'email']


class AdminQuizeQuestions(admin.ModelAdmin):
    list_display = ['id', 'question', 'ans']


class AdminLeaderBoard(admin.ModelAdmin):
    list_display = ['id', 'player', 'score']


admin.site.register(QuizeQuestions, AdminQuizeQuestions)
admin.site.register(UserData, AdminUserData)
admin.site.register(LeaderBoard, AdminLeaderBoard)