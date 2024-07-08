from django.urls import path
from .views import BoardList

app_name = 'board'

urlpatterns = [
     path('', BoardList.as_view()),
]