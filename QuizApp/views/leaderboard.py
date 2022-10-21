from django.shortcuts import render
from django.views import View

from QuizApp.models.user_info import UserData
# Create your views here.


class LeaderBoard(View):
    def post(self, request):
        return render(request, 'leaderboard.html')


    def get(self, request):
        obj = UserData.objects.filter().order_by('-score')
        return render(request, 'leaderboard.html',{'obj':obj})
    
    