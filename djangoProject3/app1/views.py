from django.shortcuts import render

# Create your views here.
def start(request):
    print('start함수 호출됨.')
    data = {"name" : "hong", "age" : 100}
    return render(request, "app1/start.html", data)