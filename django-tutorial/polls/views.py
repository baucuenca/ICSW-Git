from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"you r looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"you r voting on question {question_id}")