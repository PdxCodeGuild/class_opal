from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def index(request) -> HttpResponse:
#     question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'questions': question_list}
#     print(question_list)

#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(id=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist :( :( :(')
#     question = get_object_or_404(Question, id=question_id)
#     # choices = Choice.objects.filter(question=question)
#     return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote_helper():
    return ":)"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    thing = vote_helper()

    try:
        selection = request.POST['vote_choice']
        # choice = Choice.objects.get(id=selection)
        choice = question.choices.get(id=selection)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.pk,)))


def add_question(request):
    # question = request.POST['question']
    # new_q = Question(question_text=question)
    # new_q.save()
    new_q = Question.objects.create(question_text=request.POST['question'])
    return HttpResponseRedirect(reverse('polls:choice_page', args=(new_q.pk,)))


def choice_page(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/add-choice.html', {'question': question})


def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # choice_text = request.POST['new_choice']
    # new_c = Choice(question=question, choice_text=choice_text)
    # new_c.save()
    Choice.objects.create(
        question=question, choice_text=request.POST['new_choice'])
    return HttpResponseRedirect(reverse('polls:choice_page', args=(question.pk,)))
