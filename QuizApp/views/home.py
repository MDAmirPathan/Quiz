
from django.shortcuts import render, redirect
from django.views import View

from QuizApp.models.quize_info import QuizeQuestions
from QuizApp.models.user_info import UserData
# Create your views here.


class Home(View):
    def post(self, request):
        postData = request.POST
        first_name = request.session.get('first_name')
        user_id = request.session.get('user_id')
        try:

            print(postData, "#######",postData.get('qd.question'))
            question_data = QuizeQuestions.objects.all()
            result_data = calc_results(postData, question_data)

            if user_id:
                player = UserData.objects.filter(id=user_id).first()
                player.score = result_data['score']
                player.correct = result_data['correct']
                player.wrong = result_data['wrong']
                player.save()

            request.session['score'] = result_data['score']
            request.session['correct'] = result_data['correct']
            request.session['wrong'] = result_data['wrong']
            
            return redirect('results')
        except Exception as e:
            return render(request, 'home.html',{'error_message':e})
        


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
        if q.ans == postData.get(q.question): 
            score += 5
            correct +=1
        else:
            wrong +=1   
    result_data = {
    'score':score,
    'correct':correct,
    'wrong':wrong
    }
    return result_data


class results(View):
    def post(self,request):
        score = request.session.get('score')
        correct = request.session.get('correct')
        wrong = request.session.get('wrong')
        print('score', score,'=========================')
        result_data = {
        'score':score,
        'correct':correct,
        'wrong':wrong
        }
        return render(request, 'results.html', {
        'score':score,
        'correct':correct,
        'wrong':wrong
        })
    def get(self,request):
        score = request.session.get('score')
        correct = request.session.get('correct')
        wrong = request.session.get('wrong')
        print('score', score,'=========================')
        result_data = {
        'score':score,
        'correct':correct,
        'wrong':wrong
        }
        return render(request, 'results.html', result_data)