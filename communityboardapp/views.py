from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from testapp.models import Boards
import math


# 메인 페이지 이동
def goToMain(request):
    return render(request, 'main.html')


# 로그인 페이지 이동
# def goLogin(request):
#     return render(request, 'login.html')

def goSignUp(request):
    return render(request, 'signup.html')


# 커뮤니티 이동
def goCommunity(request):

    # page : 현재 선택한 페이지
    page = 3

    # boardsCount : 전체 게시글 개수
    boards = Boards.objects.all()
    boardsCount = boards.count()

    # initialBoard : 표기되는 첫 게시글 No / finalBoard : 표기되는 마지막 게시글 No
    initialBoard = boardsCount - 10 * (page)
    finalBoard = boardsCount - 10 * (page) + 10
    # page = math.ceil(boardsCount / 10)


    # initialPage : 표기되는 첫 페이지 / finalPage : 표기되는 마지막 페이지
    initialPage = math.trunc(page/10)*10+1

    if boardsCount > 10 * (initialPage + 9):
        finalPage = initialPage + 9
    else:
        finalPage = math.ceil(boardsCount / 10)

    pageList = []
    for i in range(initialPage, finalPage+1):
        pageList.append(i)

    print('iinitialPage: ', initialPage, ', finalPage: ', finalPage)

    # select * from Boards where id>initialBoard and id<=finalBoard order by id Desc
    boards = Boards.objects.filter(id__gt=initialBoard,
                                       id__lte=finalBoard).order_by('-id')

    return render(request, 'communityboard.html', {'boards': boards, 'pageList': pageList})



    # if page == '':
    #     page = 750
    #
    #     # 71개라 치면 1페이지일때 71부터 62까지
    #     # 2페이지면 61부터 52까지
    #     boards = Boards.objects.filter(id__gt=boardsCount - 10 * (page),
    #                                    id__lte=boardsCount - 10 * (page) + 9).order_by('-id')
    #     return render(request, 'communityboard.html', {'boards': boards})
    #
    #
    # else:
    #     page = 1
    #     boards = Boards.objects.filter(id__gt=boardsCount - 10 * (page),
    #                                    id__lte=boardsCount - 10 * (page) + 9).order_by('-id')
    #     boards = Boards.objects.filter(id__gt=boardsCount - 10, id__lte=boardsCount).order_by('-id')
    #     return render(request, 'communityboard.html', {'boards': boards})


# 회원가입
def signupCompleted(request):
    if request.method == "POST":
        username = request.POST['container__id']
        password = request.POST['container__pw']
        email = request.POST['email__id'] + '@' + request.POST['email__domain']
        phone = request.POST['container__phonenum']

        # last_name = request.POST['container__name']
        # birth = request.POST['container__birth']
        # userName = request.POST['container__id']

        # 회원가입 성공시,
        try:
            # 회원가입
            user = User.objects.create_user(username, email, password)

            # 사용자 인증과 로그인 담당
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')

        except:
            redirect('error')

        # 사용자인증 및 로그인
        # loginUser = authenticate(username=username, password=password)
        # login(request, loginUser)

    return redirect('error')


# 아이디 중복 확인
def userIdCheck(request):
    if request.method == "POST":
        username = request.POST.get('username', False)

    else:
        username = ''

    idObject = User.objects.filter(username__exact=username)
    idCount = idObject.count()

    if idCount > 0:
        msg = "<font color='red' display='block'>이미 존재하는 아이디입니다.</font><input type='hidden'" \
              "name='idcheck__result' id='idcheck__result' value=0/>"

    else:
        msg = "<font color='green'>사용가능한 아이디입니다.</font><input type='hidden'" \
              "name='idcheck__result' id='idcheck__result' value=0/>"

    return HttpResponse(msg)


def loginCompleted(request):
    return render(request, 'main.html')


def goErrorPage(request):
    return render(request, 'errorpage.html')

# def goRegistUser(request):
#  # return redirect('accounts:login')
