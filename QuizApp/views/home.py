from logging import exception
from django.shortcuts import render
from django.views import View

from QuizApp.models.quize_info import QuizeQuestions
# Create your views here.


class Home(View):
    def post(self, request):
        postData = request.POST
        first_name = request.session.get('first_name')
        user_id = request.session.get('user_id')

        print(postData, "#######",postData.get('qd.question'))
        question_data = QuizeQuestions.objects.all()
        result_data = calc_results(postData, question_data)
        context={
            'result_data':result_data
        }
        return render(request, 'home.html', context)
        


    def get(self, request):
        first_name = request.session.get('first_name')
        user_id = request.session.get('user_id')
        question_data = QuizeQuestions.objects.all()
        context={
            'question_data': question_data,
            'first_name':first_name
        }
        
        return render(request, 'home.html', context)
    

def calc_results(postData, question_data)->dict:
    score = 0
    correct = 0
    wrong = 0
    for q in question_data:
        print(q, q.ans ,postData.get('qd.question') )
        print("================")


    result_data = {
    'score':score,
    'correct':correct,
    'wrong':wrong
    }
    return result_data
