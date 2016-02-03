from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from cellar.models import Beer, UploadedUntappdCSV, Brewery, Style


def beer_view(request, beer_id=None):
    beer = Beer.objects.get(pk=int(beer_id))

    context = {
        'beer': beer
    }

    return render_to_response('beer.html', context)


def brewery_view(request, brewery_id=None):
    brewery = Brewery.objects.get(pk=int(brewery_id))
    beers = Beer.objects.filter(brewery=brewery)

    context = {
        'brewery': brewery,
        'beers': beers,
    }

    return render_to_response('brewery.html', context)


def style_view(request, style_id=None):
    style = Style.objects.get(pk=int(style_id))
    beers = Beer.objects.filter(style=style)

    context = {
        'style': style,
        'beers': beers,
    }

    return render_to_response('style.html', context)
