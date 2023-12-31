from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .froms import AnswerForm, QuestionForm
from .models import Answer, Question
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    list_elem_number = 5
    paginator = Paginator(question_list, list_elem_number)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()

            return redirect('pybo:detail', question_id=question_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question': question, 'form': form}
    
    return render(request, 'pybo/question_detail.html', context)

def answer_delete(request, question_id, answer_id):
    Answer.objects.get(pk = answer_id, question_id=question_id).delete()

    return redirect('pybo:detail', question_id=question_id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()

            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}

    return render(request, 'pybo/question_form.html', context)

def question_delete(request, question_id):
    Question.objects.get(pk = question_id).delete()
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)