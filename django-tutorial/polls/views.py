from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F #operaciones de referencia a campos de la base de datos
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last five published questions.
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Volver a mostrar el form de la pregunta para votar
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 # se realiza el incremento en la base de datos
        selected_choice.save()
        # Siempre redirigir después de procesar el POST para evitar el reenvío del formulario al actualizar la página.
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))