from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import authenticate, login
from datetime import datetime
from testapp import models
from .models import Boards, BoardCategories, AuthUser, BoardComment
import math
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.hashers import check_password
# from .forms import boardsForm


# 메인 페이지 이동
def goToMain(request):
    return render(request, 'main.html')


def goSignUp(request):
    return render(request, 'signup.html')


# Board 테이블 표기 및 페이징, 커뮤니티 이동
def goCommunity(request):
    allBoards = Boards.objects.all().order_by("-id")

    # page = 요청된 페이지. default 1
    page = int(request.GET.get('page', 1))
    print(page)

    # 페이지당 보여줄 게시글 개수 설정
    paginator = Paginator(allBoards, 20)

    # 페이징 객체 설정 : 요청된 페이지에 해당하는 페이징 객체 설정
    # 표기될 페이지 개수
    boards = paginator.get_page(page)

    # 전체 게시글 개수
    boardsCount = Boards.objects.all().count()
    num_pages = paginator.num_pages

    # initialPage : 표기되는 첫 페이지 / finalPage : 표기되는 마지막 페이지
    initialPage = math.trunc((page - 1) / 10) * 10 + 1

    if boardsCount > 10 * (initialPage + 9):
        finalPage = initialPage + 9
    else:
        finalPage = math.ceil(boardsCount / 10)

    pageList = []
    for i in range(initialPage, finalPage + 1):
        pageList.append(i)

    # 이전, 다음 페이지 클릭시 넘어갈 페이지 값
    previousPage = math.trunc((page - 1) / 10) * 10
    nextPage = math.ceil(page / 10) * 10 + 1

    return render(request, 'communityboard.html',
                  {'boards': boards, 'pageList': pageList, 'previousPage': previousPage, 'nextPage': nextPage,
                   'numPages': num_pages})


# 게시글 쓰기 페이지 이동
@login_required
def writePost(request):
    # writePostForm = boardsForm()

    return render(request, 'writepost.html')
    # return render(request, 'writepost.html', {'writePostForm': writePostForm})


@login_required
def boardwriteCompleted(request):


    # # post 방식으로 넘어오고 데이터들이 올바른 형식이면 데이터 베이스에 저장
    # if request.method == "POST":
    #     writePostForm = boardsForm(request.POST)
    #
    #     if writePostForm.is_valid():
    #         writePostForm.save()
    #         return redirect('/community')
    #
    #     # else:
    #     #     return redirect('index')
    #
    # else:
    #     writePostForm = boardsForm()
    #     return render(request, 'writepost.html', {'writePostForm': writePostForm})

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        user = AuthUser.objects.get(username=request.user)
        # user = request.POST['user']
        category = BoardCategories.objects.get(id=1)

        print('제목: ', title, '  내용: ', content, '  작성자:', user)

        try:
            img_file = request.POST['img_file']

        except:
            img_file = None

    else:
        title = None

    # 게시글 작성 성공 시
    try:
        category = BoardCategories.objects.get(id=1)
        if title != None:
            # if request.user and title and content and request.user.is_superuser >= category.authority:
            article = Boards(category=category, user=user, title=title, content=content, image=img_file)
            article.save()

            print('1')
            return redirect('/community')

        else:
            print('2')
            return redirect('/error')

    # 게시글 작성 실패 시
    except:
        print('3')
    # return redirect('/error')


# print('4')
# return redirect('/community')


# 회원가입완료
def signupCompleted(request):
    username = request.POST['container__id']
    password = request.POST['container__pw']
    email = request.POST['email__id'] + '@' + request.POST['email__domain']
    phone = request.POST['container__phonenum']
    last_name = request.POST['container__name']
    date_birth = request.POST['container__birth']

    # 회원가입완료
    user = AuthUser.objects.create_user(username, password, last_name, email, phone, date_birth)

    # 사용자 인증 및 로그인
    user = authenticate(username=username, password=password)
    login(request, user)

    return redirect('/')

    # # if request.method == "POST":
    #     username = request.POST['container__id']
    #     password = request.POST['container__pw']
    #     email = request.POST['email__id'] + '@' + request.POST['email__domain']
    #     phone = request.POST['container__phonenum']
    #     last_name = request.POST['container__name']
    #     date_birth = request.POST['container__birth']
    #
    #     # 회원가입완료
    #     user = User.objects.create_user(username, password, last_name, email, phone, date_birth)
    #
    #     # 사용자 인증 및 로그인
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #
    #     return redirect('/')
    #
    #     # # 회원가입 성공시,
    #     # try:
    #     #     # 회원가입
    #     #     # user = User.objects.create_user(username, email, password, {'phone': phone, 'date_birth': date_birth, 'last_name': last_name})
    #     #     user = User.objects.create_user(username, email, password, {phone, last_name})
    #     #
    #     #
    #     #     # 사용자 인증과 로그인 담당
    #     #     user = authenticate(username=username, password=password)
    #     #     login(request, user)
    #     #
    #     #     return redirect('/')
    #     #
    #     # except:
    #     #     redirect('error')
    #
    #     # 사용자인증 및 로그인
    #     # loginUser = authenticate(username=username, password=password)
    #     # login(request, loginUser)
    #
    # # else:
    # # return redirect('error')


# 아이디 중복 확인
def userIdCheck(request):
    if request.method == "POST":
        username = request.POST.get('username', False)

    else:
        username = ''

    idObject = AuthUser.objects.filter(username__exact=username)
    idCount = idObject.count()

    if idCount > 0:
        msg = "<font color='red' display='block'>이미 존재하는 아이디입니다.</font><input type='hidden'" \
              "name='idcheck__result' id='idcheck__result' value=0/>"

    else:
        msg = "<font color='green'>사용가능한 아이디입니다.</font><input type='hidden'" \
              "name='idcheck__result' id='idcheck__result' value=0/>"

    return HttpResponse(msg)


# 로그인완료
def loginCompleted(request):
    return render(request, 'main.html')


# 에러페이지 이동
def goErrorPage(request):
    return render(request, 'errorpage.html')


# 게시글 자세히
def viewBoard(request, id):
    try:
        boardComment = BoardComment.objects.filter(article__id=id).order_by('id')
        board = Boards.objects.get(id=id)

    except Exception as e:
        Boards.DoesNotExist
        print(e)
        raise Http404("Does not exist!")

    return render(request, 'viewboard.html', {'boardComment': boardComment, 'boardId': id, 'board': board})


# 댓글삽입
@login_required
def insertComment(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        content = request.POST.get('content', False)
        boardId = request.POST.get('boardId', False)

        board = Boards.objects.get(id=boardId)
        user = AuthUser.objects.get(id=username)

        # insert into board_comment (id, board_id, username, registered_date, content) values (#, board.id, username,now(), content);
        boardComment = BoardComment(article=board, user=user, content=content, reference_reply_id='4')
        boardComment.save()

        comment = BoardComment.objects.filter(article=board).order_by('-registered_date')

        context = {
            'content': content,
            'username': username,
            'registered_date': boardComment.registered_date
        }

        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")

# 게시글 삭제
@login_required
def deleteBoard(request, id):
    board = Boards.objects.get(id=id)
    board.delete()
    return redirect('/community')
