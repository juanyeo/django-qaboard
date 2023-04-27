from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question

# Create your views here.

def question_list(request):
    context = {'question_list' : Question.objects.all()}
    return render(request, "write/question_list.html", context)

def question_form(request):
    if request.method == "GET":
        form = QuestionForm()
        return render(request, "write/question_form.html", {'form': form})
    elif request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/question/")


def question_delete(request, id):
    question = Question.objects.get(pk=id)
    question.delete()

    return redirect("/question/")