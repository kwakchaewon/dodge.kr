from django.urls import path
from communityboardapp.views import goToMain, goLogin, goSignUp, goCommunity, signupCompleted, userIdCheck,userPasswordCheck

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    # path('url', view, name=''),
    path('', goToMain, name='main'),
    path('login', goLogin,),
    path('signup', goSignUp,),
    path('community', goCommunity, ),
    path('signupCompleted', signupCompleted, ),
    path('userIdCheck', userIdCheck),
    path('userPasswordCheck', userPasswordCheck),
]