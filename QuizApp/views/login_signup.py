from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password

from QuizApp.models.user_info import UserData

# Create your views here.


class SignUp(View):
    def post(self, request):
        try:
            postData = request.POST
            first_name = postData.get('FirstName')
            last_name = postData.get('LastName')
            email = postData.get('email')
            password = postData.get('password')
            password1 = postData.get('password1')
            
            error_message = None

            register_user = UserData(first_name=first_name,
                                    last_name= last_name,
                                    email=email,
                                    password=password
            )

            valid_data, error_message = validate_user(postData)
            if not valid_data:
                return render(request, 'signup.html', {'error_message': error_message})

            password_hash = make_password(password)
            register_user.password = password_hash
            register_user.register()
            request.session['player_id'] = UserData.objects.filter(email=email).first().id
            return redirect('home_page')
           
        except Exception as e:
            print(e)
            return render(request, 'signup.html', {'error_message': e})


    def get(self, request):
        return render(request, 'signup.html')
    
def validate_user(postData):
    error_message = None
    try:
        first_name = postData.get('FirstName')
        email = postData.get('email') 
        password = postData.get('password') 
        password1 = postData.get('password1')
        
        if first_name == None or type(first_name)!= type('string')or len(first_name)<4:
            return False, 'Plese Enter First Name Correctly minimun 4 charectors'
        if email == None or type(email)!= type('string') or UserData.isExists(email):
            return False, 'Email Is Wrong Or Alrady Exists '

        if password == None or len(password)<8:
            return False, 'Plese Enter Password Correctly minimun 8 charectors'
        if password != password1:
            return False, 'Password Does not Match'

    except Exception as e:
        return False, e
    return True, ''
    
    

class LogIn(View):
    def post(self, request):
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        
        return render(request, 'login.html')


    def get(self, request):
        return render(request, 'login.html')
    
    
