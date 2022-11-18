from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello world')


# Made it this way at first because it seemed to be the way it was taught.

class SquaringView(View):
    def get(self,  request, number):
        if (request):
            print(number * number)
            return HttpResponse(number * number)
        else:
            return HttpResponse(request)


# Create your views here.
