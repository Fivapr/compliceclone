from django.shortcuts import render
from .forms import Goal_form
from django.utils import timezone
from django.shortcuts import redirect
from .models import Goal

def index(request):
    return render(request, 'index.html', {})

def goals(request):
    if request.user.is_authenticated:
        goals = Goal.objects.filter(author=request.user)

        if request.method == 'POST':
            form = Goal_form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
            return redirect('/goals', )
        else:
            form = Goal_form()
            return render(request, 'goals.html', {'form': form, 'goals': goals})
    else:
        return redirect('/login', )

def test_view(request):
    return render(request, 'test.html', {})