from django.urls import path
from communityboardapp.views import goToMain, goLogin, goSignUp, goCommunity

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    path('', goToMain,),
    path('login', goLogin,),
    path('signup', goSignUp,),
    path('community', goCommunity, ),
]