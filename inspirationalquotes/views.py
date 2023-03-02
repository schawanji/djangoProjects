from django.shortcuts import render
import random

quotesList = ["When you have a dream, you've got to grab it and never let go.",
              "Nothing is impossible",
              "There is nothing impossible to they who will try.",
              "The bad news is time flies",
              "Life has got all those twists and turns",
              "Keep your face always toward the sunshine, and shadows will fall behind you."]
# Create your views here.


def quotes(request):
    quote = random.choice(quotesList)
    context = {'quote': quote, 'quotes': quotesList}
    return render(request, 'inspirationalquotes/home.html', context)


