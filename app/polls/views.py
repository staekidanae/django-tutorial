from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    # 최신 질문들을 정리하는데 pub_date를 역순으로 0~4번째까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output을 "질문명, 질문내용" 으로 저장
    context = {
        'latest_question_list': latest_question_list,
    }

    template = loader.get_template('polls/index.html')
    html = template.render(context, request)
    # output을 웹 응답으로 송신 및 출력
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
