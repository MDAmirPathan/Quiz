from django.shortcuts import render
from django.views import View
# Create your views here.


class LeaderBoard(View):
    def post(self, request):
        return render(request, 'leaderboard.html')


    def get(self, request):
        return render(request, 'leaderboard.html')
    
    