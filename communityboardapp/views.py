from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# 메인 페이지 이동
def goToMain(request):
    return render(request, 'main.html')

# 로그인 페이지 이동
def goLogin(request):
    return render(request, 'login.html')

def goSignIn(request):
    return render(request, 'login.html')

def goSignUp(request):
    return render(request, 'signup.html')

# 커뮤니티 이동
def goCommunity(request):
    return render(request, 'community.html')

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

        # 회원가입
        user = User.objects.create_user(username, password, email)

        # 사용자인증 및 로그인
        # loginUser = authenticate(username=username, password=password)
        # login(request, loginUser)


        return redirect('/')
    return render(request, 'errorpage.html')


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

# def goRegistUser(request):
#  # return redirect('accounts:login')