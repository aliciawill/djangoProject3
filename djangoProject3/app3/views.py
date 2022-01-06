from django.shortcuts import render

# Create your views here.
def start3(request):
    # print('받은 데이터 n1>>  ', request.GET['n1'])
    # print('받은 데이터 n2>>  ', request.GET['n1'])
    print('start3함수 호출됨.')
    n1 = 100
    n2 = 300
    result = n1 + n2
    # context = {"result" : request.GET['n1'] + request.GET['n2']}
    context = {"result" : result, "n1" : n1, "n2" : n2}
    return render(request, "app3/start3.html", context)