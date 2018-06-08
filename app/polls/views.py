from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
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

def custom_get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404()

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = custom_get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
    }
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    # question_id 해당하는 Question 인스턴스 전달
    # 템플릿 (polls/templates/polls/results.html
    # Question의 question_tesxt를 보여주고
    # Question에 연결된 Choice목록과 vote수를 보여준다
    # {% for %} loop구문과
    # question.choice_set.all 을 사용

    question = Question.objects.get(id=question_id)
    # choice_id = request.POST['choice']
    # choice = Choice.objects.get(id=choice_id)
    # choice_text = choice.choice_text
    # choice_votes = choice.votes

    context = {
        'question' : question,
        # 'choice' : choice,
        # 'choice_text' : choice_text,
        # 'choice_votes' : choice_votes
    }

    return render(request, 'polls/results.html', context)

def vote(request, question_id):

    # print('request.get : ', request.GET)
    # print('request.POST : ', request.POST)
    # 선택한 choice의 choice_text와 id값을 갖는 문자열 생성
    question = Question.objects.get(id=question_id)
    question_text = question.question_text

    choice_id = request.POST['choice']
    choice = Choice.objects.get(id=choice_id)
    choice_text = choice.choice_text

    choice.votes += 1
    choice.save()

    choice_votes = choice.votes

    result = 'question_text : {}, choice_text: {}, choice.id: {}, choice_votes: {}'.format(
        question_text,
        choice_text,
        choice_id,
        choice_votes,
    )
    url = '/polls/{}/results/'.format(question_id)
    return HttpResponseRedirect(url)

    url = reverse('polls:results', args=[question_id])
    return HttpResponseRedirect(url)