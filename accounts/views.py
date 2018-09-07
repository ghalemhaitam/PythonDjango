from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, request
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def LoginView(request):

    if User is not None:
        # do something if the user is authenticated
        return redirect('/account/')
    else:
        # do something if the user is authenticated
        return render(request,'account/login.html')
   




def DashbordUser(request):
    return render(request,'account/dashbord_user.html')




def LogoutUser(request):
    
    
    if logout(request):
        return render(request, 'account/login.html')
    else:
        return render(request, 'account/dashbord_user.html')

      
    




class InscriptionView(generic.ListView):
    template_name = 'account/inscription.html'
    def get_queryset(self):
        return




def Authentification(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                return HttpResponse("yes")
            else:
                return HttpResponse("yes,no")
        
        else:
            # No backend authenticated the credentials
            return HttpResponse("no")
    else:
        return HttpResponse("no")
        #return redirect('/account/')


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