from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from cellar.models import Beer, UploadedUntappdCSV


def beer_view(request):
    beer = Beer.objects.first()

    context = {
        'beer': beer
    }

    return render_to_response('beer.html', context)
