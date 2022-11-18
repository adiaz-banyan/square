from django.urls import path
from squaring.views import HelloWorldView

urlpatterns = [
    path('', HelloWorldView.as_view()),

]
