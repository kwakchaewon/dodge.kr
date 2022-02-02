from django.urls import path
from communityboardapp.views import goToMain, goLogin

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    path('', goToMain,),
    path('login', goLogin,),
]