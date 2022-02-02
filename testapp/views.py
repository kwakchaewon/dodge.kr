from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from testapp.models import Boards

# Create your views here.


# Class Based View 예제
# Generic view인 ListView를 상속받는다.
# 템플릿을 따로 지정할 필요없이 뷰에서 지정한 model의 이름을 사용하여 '앱디렉토리/모델명_list.html' 템플릿 파일을 사용한다.
# testapp/boards_list.html
class BoardListClassView(ListView):
    model = Boards

    def BoardFunctionView(request):
        boardList = Boards.objects.all()

        return render(request, 'boardsfunctionview.html', {'boardList': boardList})



# Generic view인 TemplateView를 상속받는다.
# template_name을 지정한다.
# template.html
class BoardsTemplateClassView(TemplateView):
    template_name = "template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Boards.objects.all()
        return context




# Function Based View 예제
# render 함수에 의해 boardsfunctionview.html 반환
def BoardsFunctionView(request):
    boardList = Boards.objeccts.all()

    return render (request,'boardsfunctionview.html',{'boardList':boardList})



# query sey select() 예제
def selectSomething(request):
    # all(): 테이블상 모든 데이터셋
    # filter(): 특정 조건에 부합하는 데이터셋
    # excluded(): 특정 조건을 제외한 데이터셋
    # get(): 특정 조건에 부합하는 1개의 데이터셋
    # count(): 개수
    # last(): 가장 마지막 데이터셋
    # exist(): 데이터 유무
    # order_by(): 특정 필드 순서대로 정렬

    Boards.objects.all()
    Boards.objects.filter(category_name__exact='free')
    Boards.objects.exclued(user_id__exact='test')
    Boards.objects.get(id=3)
    Boards.objects.all().count()



# 요청된 정보에 응답하기

# render는 웹사이트 요청응답시 템플릿 파일이름과 파일 내에서 사용할 변수를 지정할 때 사용된다.
def BoardView(request):
    boardList = Boards.object.all()
    return render(request,'boardsview.html',{'board' : boardList})


# redirect는 특정 URL로 페이지를 이동할 때 사용된다.
# 요청에 대해 해당하는 템플릿 파일을 반환하는 render와는 다르게 redirect는 다른 URL로 이동한다.
def board_delete_result(request):
    return redirect()


# HttpResponse는 웹사이트 요청시 간단한 응답을 위한 객체이다.
# template으로 사용할 파일을 반환하지 않고 응답을 위한 문자열을 반환한다.
def user_register_idcheck(request):
    msg = "이미 존재하는 id 입니다"

    return HttpResponse(msg)