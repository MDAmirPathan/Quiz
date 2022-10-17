from django.shortcuts import render
from django.views import View

from QuizApp.models.quize_info import QuizeQuestions
# Create your views here.


class Home(View):
    def post(self, request):
        first_name = request.session.get('first_name')
        user_id = request.session.get('user_id')
        
        return render(request, 'home.html')


    def get(self, request):
        first_name = request.session.get('first_name')
        user_id = request.session.get('user_id')
        question_data = QuizeQuestions.objects.all()
        context={
            'question_data': question_data,
            'first_name':first_name
        }
        return render(request, 'home.html', context)
    
    