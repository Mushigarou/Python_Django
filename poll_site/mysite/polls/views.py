from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# from django.template import loader

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions" : latest_questions}
    return HttpResponse(render(request, "polls/index.html", context))

def detail(request, question_id):
    # try :
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Questions does not exist')
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", { "question" : q })

def results(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)