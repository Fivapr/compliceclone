from django.shortcuts import render
from django.http import HttpResponseRedirect
from complice.forms import RegistrationForm

def register(request):

    form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html', {})

# Create your views here.
#def drinker_reg(request):
    #if request.user.is_authenticated():
    #      return HttpResponseRedirect('/profile/')
    #if request.method == 'POST':
    #     pass
    #else:
    #     ''' user is not submitting the form, show them a blank registration form '''
