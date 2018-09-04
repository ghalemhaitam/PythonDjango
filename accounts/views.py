from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, request
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.

class LoginView(generic.ListView):

    """
    if User is not None:
       # do something if the user is authenticated
         redirect('/crud/')
    else:
       # do something if the user is authenticated
        template_name = 'account/login.html'
   
    """

    template_name = 'account/login.html'
    def get_queryset(self): 
        return


class InscriptionView(generic.ListView):
    template_name = 'account/inscription.html'
    def get_queryset(self):
        return


def Inscription(request):
    """
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'posts/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('posts:results', args=(question.id,)))
    
   """ 