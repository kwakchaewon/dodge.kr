from django.urls import path
from communityboardapp.views import goToMain, goSignUp, goCommunity, \
    signupCompleted, userIdCheck, loginCompleted, goErrorPage, index
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    # path('url', view, name=''),
    path('', goToMain, name='main'),
    # path('login', goLogin,),
    path('signup', goSignUp,),
    path('community', goCommunity, ),
    path('signupCompleted', signupCompleted, ),
    path('userIdCheck', userIdCheck),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login.html'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('error', goErrorPage),
]