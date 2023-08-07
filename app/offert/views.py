from django.http import HttpResponse, Http404
from .models import Offert
from django.shortcuts import render,get_object_or_404

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "offert/detail.html")

def detail(request, question_id):
    offert = get_object_or_404(Offert, pk=question_id)
    return render(request, "offert/detail.html", {"question": offert})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)