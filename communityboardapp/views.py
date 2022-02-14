from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from testapp.models import Boards
import math
from django.core.paginator import Paginator



# 메인 페이지 이동
def goToMain(request):
    return render(request, 'main.html')


# 로그인 페이지 이동
# def goLogin(request):
#     return render(request, 'login.html')

def goSignUp(request):
    return render(request, 'signup.html')


# Board 테이블 표기 및 페이징, 커뮤니티 이동
def goCommunity(request):

    # page : 현재 선택한 페이지
    page = int(request.GET.get('page', 1))

    # boardsCount : 전체 게시글 개수
    boards = Boards.objects.all()
    boardsCount = boards.count()

    # 총 페이지 수
    totPage = math.ceil(boardsCount / 10)


    # # 처음, 이전, 다음, 끝 버튼 누를 경우 실행
    # pageCal = str(request.GET.get('page', ''))
    #
    # if pageCal == 'first':
    #     page = 1
    #     print('성공')
    # elif pageCal == 'previous':
    #     page = math.trunc(math.trunc(page/10) * 10 - 1) + 1
    # elif pageCal == 'next':
    #     page = math.ceil(page/10)*10 + 1
    # elif pageCal == 'last':
    #     page = totPage




    # initialBoard : 표기되는 첫 게시글 No / finalBoard : 표기되는 마지막 게시글 No
    initialBoard = boardsCount - 10 * (page) + 1
    finalBoard = boardsCount - 10 * (page) + 10


    # initialPage : 표기되는 첫 페이지 / finalPage : 표기되는 마지막 페이지
    initialPage = math.trunc((page-1)/10)*10 + 1

    if boardsCount > 10 * (initialPage + 9):
        finalPage = initialPage + 9
    else:
        finalPage = math.ceil(boardsCount / 10)

    pageList = []
    for i in range(initialPage, finalPage+1):
        pageList.append(i)


    # 현재 페이지가 1 ~ 10 페이지 사이 or 총 페이지 <= 10
    # 처음, 이전 버튼 표기한다 (pageAble1 = 1) / 처음, 이전 버튼 표기하지않는다 (pageAble1 = 0)
    if page <= 10:
        pageAble1 = 0
    elif totPage <= 10:
        pageAble1 = 0
    else:
        pageAble1 = 1

    # 다음, 마지막 버튼 표기한다 (pageAble2 = 1) / 다음, 마지막 버튼 표기하지않는다 (pageAble2 = 0)
    if math.floor(page) == math.floor(totPage):
        pageAble2 = 0
    else:
        pageAble2 = 1


    # select * from Boards where id>initialBoard and id<=finalBoard order by id Desc
    boards = Boards.objects.filter(id__gt=initialBoard,
                                       id__lte=finalBoard).order_by('-id')

    return render(request, 'communityboard.html', {'boards': boards, 'pageList': pageList, 'pageAble1': pageAble1, 'pageAble2' : pageAble2, 'page':page})


# def index(request):
#     page = request.GET.get('page', '1')
#     boardList = Boards.objects.order_by('-id')
#
#     # 페이지당 10개씩 보여준다.
#     paginator = Paginator(boardList, 10)
#
#
#     pagObj = paginator.get_page(page)
#
#     context = {'boardList': boardList}
#
#     return render(request, 'communityboard.html', context)



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
