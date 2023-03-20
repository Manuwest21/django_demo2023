from django.shortcuts import render
from .functions import mult_5
# from .models import Functionality
from django.views.generic import ListView



def home (request):
    # import pudb; pu.db()
    weekdays=[
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'samedi',
        'dimanche',
    ]
    
    
    context = {'test': mult_5(30),
               "testi": weekdays}
    return render (request, 'ppale/home.html', context=context)


def about (request):
    
   
    return render (request, 'ppale/about.html')

