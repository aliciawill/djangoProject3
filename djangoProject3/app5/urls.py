from django.urls import path, include
import app5.views


# http://localhost:5555/app5
urlpatterns = [
    path('', app5.views.start5),
    path('/js01', app5.views.js01, name='js01'),
    #path('/insert') #http://localhost:5555/app5/insert
]
