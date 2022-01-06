from django.http import HttpResponse


def index(request):
    return HttpResponse("<body bgcolor=green>" +
                        "<hr>" +
                        "<h1>첫 페이지 입니다.</h1>" +
                        "<hr>" +
                        "<a href=start>to start page</a><br>" +
                        "<a href=start2>to start2 page</a><br>" +
                        "<a href=admin>to admin page</a><br>"
                        "</body>")