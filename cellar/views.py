from django.shortcuts import render, render_to_response
from cellar.models import Beer


def beer_view(request):
    beer = Beer.objects.first()

    context = {
        'beer': beer
    }

    return render_to_response('beer.jinja2', context)
