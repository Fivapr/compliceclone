from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def createroom(request):
    return render(request, 'createroom.html', {})

def rooms(request):
    return render(request, 'rooms.html', {})

def features(request):
    return render(request, 'features.html', {})

def legalstuff(request):
    return render(request, 'legalstuff.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def newsletter(request):
    return render(request, 'newsletter.html', {})

def fivapr(request):
    return render(request, 'fivapr.html', {})

def fivapr_today(request):
    return render(request, 'fivapr_today.html', {})

def fivapr_settings(request):
    return render(request, 'Fivapr_settings.html', {})

def fivapr_reviews(request):
    return render(request, 'Fivapr_reviews.html', {})

def fivapr_reviews_2016_Jul(request):
    return render(request, 'Fivapr_reviews_2016_Jul.html', {})

def fivapr_reviews_2016_week_30(request):
    return render(request, 'Fivapr_reviews_2016_week_30.html', {})

def fivapr_goals(request):
    return render(request, 'Fivapr_goals.html', {})

def fivapr_refer(request):
    return render(request, 'Fivapr_refer.html', {})