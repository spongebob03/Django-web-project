from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    return render(request, 'index.html', {"question_list": question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'question': question})

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('detail', question_id=question.id)