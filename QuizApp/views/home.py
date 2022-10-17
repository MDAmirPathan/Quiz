from winreg import QueryInfoKey
from django.shortcuts import render
from django.views import View

from QuizApp.models.quize_info import QuizeQuestions
# Create your views here.


class Home(View):
    def post(self, request):
        return render(request, 'home.html')


    def get(self, request):
        question_data = QuizeQuestions.objects.all()
        context={
            'question_data': question_data,
        }
        return render(request, 'home.html', context)
    
    