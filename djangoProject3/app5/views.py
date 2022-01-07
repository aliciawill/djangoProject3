from django.shortcuts import render

# Create your views here.
def start5(request):
    print('==================== start5호출됨.')
    context = {"today" : "금요일", "when" : "2022년 1월 7일"}
    return render(request, "app5/start5.html", context)

def js01(request):
    print('=================== js01호출됨.')
    return render(request, "app5/js01.html")