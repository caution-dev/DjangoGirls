from django.http import HttpResponse
from django.shortcuts import render


def post_list_raw(request):
    return HttpResponse('Post List!')


# html 파일 템플릿을 불러와서 렌더링 > HttpResponse 로 돌려준다.
def post_list(request):
    return render(request, 'post_list.html')
