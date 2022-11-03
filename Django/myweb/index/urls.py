from django.urls import path
from .views import Mainpage

urlpatterns = [
    path('index/',Mainpage.as_view()),
]