from django.urls import path
from django.contrib.auth import views as auth_views
from communityboardapp.views import *

urlpatterns = [
    # path('cbvList', BoardListClassView.as_view(), name='cbv'),
    # path('url', view, name=''),
    path('', goToMain, name='main'),
    path('signup', goSignUp, ),
    path('community', goCommunity, name='community'),
    path('community/write', writePost, name='writePost'),
    path('writenotice', writeNotice, name='writeNotice'),
    path('boardwritecompleted', boardwriteCompleted, name='boardwriteCompleted'),
    path('noticewritecompleted', noticeWriteCompleted, name='noticeWriteCompleted'),
    path('signupcompleted', signupCompleted, ),
    path('useridcheck', userIdCheck, ),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('error', goErrorPage),
    path('viewboard/<int:id>/', viewBoard, name='viewboard'),
    path('insertComment', insertComment, name='insertComment'),
    path('deleteboard/<int:id>/', deleteBoard, name='deleteBoard'),
    path('editboard/<int:id>/', editBoard, name='editBoard'),
    path('editboardCompleted', editBoardCompleted, name='editBoardCompleted'),
    path('boardthumbUp', boardThumbUp, name='boardThumbUp'),
    path('boardthumbDown', boardThumbDown, name='boardThumbDown'),
    path('searchboard', searchBoard, name='searchBoard'),
]
