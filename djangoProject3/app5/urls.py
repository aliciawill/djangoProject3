from django.urls import path, include
import app5.views


# http://localhost:5555/app5
# path('/insert') #http://localhost:5555/app5/insert
urlpatterns = [
    path('', app5.views.start5),
    path('/js01', app5.views.js01, name='js01'),
    path('/js02', app5.views.js02, name='js02'),
    path('/js03', app5.views.js03, name='js03'),
    path('/js04', app5.views.js04, name='js04'),
    path('/js05', app5.views.js05, name='js05'),
    path('/js06', app5.views.js06, name='js06'),
]
