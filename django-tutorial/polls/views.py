from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("you r at the polls index")

def detail(request, question_id):
    return HttpResponse(f"you r looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"you r looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"you r voting on question {question_id}")