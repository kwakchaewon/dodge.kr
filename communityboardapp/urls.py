from django.urls import path
from django.contrib.auth import views as auth_views
from communityboardapp.views import *

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    # path('url', view, name=''),
    path('', goToMain, name='main'),
    path('signup', goSignUp, ),
    path('community', goCommunity, name='community'),
    path('community/write', writePost, ),
    path('boardwriteCompleted', boardwriteCompleted, name='boardwriteCompleted'),
    path('signupCompleted', signupCompleted, ),
    path('userIdCheck', userIdCheck, ),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('error', goErrorPage),
    path('viewboard/<int:id>/', viewBoard, name='viewboard'),
    path('insertComment', insertComment, name='insertComment'),
    path('deleteBoard/<int:id>/', deleteBoard, name='deleteBoard'),
    path('editBoard/<int:id>/', editBoard, name='editBoard'),
    path('editBoardCompleted', editBoardCompleted, name='editBoardCompleted'),
    path('boardThumbUp', boardThumbUp, name='boardThumbUp'),


]
