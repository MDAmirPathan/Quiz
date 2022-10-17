from django.urls import path
from .views.home import Home
from .views.login_signup import LogIn,SignUp
from .views.leaderboard import LeaderBoard
urlpatterns = [
    path('', Home.as_view(), name='home_page'),
    path('login/', LogIn.as_view(), name='login_page'),
    path('signup/', SignUp.as_view(), name='signup_page'),
    path('leaderboard/', LeaderBoard.as_view(), name='leaderboard_page'),
]