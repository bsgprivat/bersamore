import re
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from cellar.models import Beer, UploadedUntappdCSV, Brewery, Style, Country


@csrf_exempt
def beerfinder(request):
    beers = Beer.objects.all()
    styles = Style.objects.all()
    breweries = Brewery.objects.all()
    filter = False
    filter_brewery = False
    filter_name = None
    filter_style = 0

    if request.POST:
        if 'name' in request.POST:
            filter_name = request.POST['name']
            if bool(filter_name):
                beers = beers.filter(name__iregex=re.escape(filter_name))
                filter = True
                
        if 'brewery' in request.POST:
            filter_brewery = request.POST['brewery']
            if int(filter_brewery) > 0:
                beers = beers.filter(brewery__id=int(filter_brewery))
                filter = True

        if 'style' in request.POST:
            filter_style = request.POST['style']
            if int(filter_style) > 0:
                beers = beers.filter(style__id=int(filter_style))
                filter = True

        if 'country' in request.POST:
            filter_country = request.POST['country']
            if filter_country:
                beers = beers.filter(brewery__country__id=int(filter_country))
                filter = True

        if 'hops' in request.POST:
            filter_hops = request.POST['hops']
            if filter_hops:
                beers = beers.filter(name__iregex=re.escape(filter_hops))
                filter = True

        if 'ibu_from' in request.POST:
            filter_ibu_from = request.POST['ibu_from']
            if filter_ibu_from:
                beers = beers.filter(ibu__gte=int(filter_ibu_from))
                filter = True
        if 'ibu_to' in request.POST:
            filter_ibu_to = request.POST['ibu_to']
            if filter_ibu_to:
                beers = beers.filter(ibu__lte=int(filter_ibu_to))
                filter = True

        if 'abv_from' in request.POST:
            filter_abv_from = request.POST['abv_from']
            if filter_abv_from:
                beers = beers.filter(abv__gte=float(filter_abv_from))
                filter = True
        if 'abv_to' in request.POST:
            filter_abv_to = request.POST['abv_to']
            if filter_abv_to:
                beers = beers.filter(abv__lte=float(filter_abv_to))
                filter = True

    return render_to_response('beerfinder.html', locals())


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

def beer_view(request, beer_id=None):
    beer = Beer.objects.get(pk=int(beer_id))

    context = {
        'beer': beer,
    }

    return render_to_response('beer_view.html', context)
