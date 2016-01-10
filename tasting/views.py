from django.shortcuts import render, render_to_response
from tasting.models import Checkin, TastingSession


def checkin_view(request):
    checkin = Checkin.objects.first()
    tasting = checkin.tasting

    context = {
        'checkin': checkin,
        'tasting': tasting
    }

    return render_to_response('checkin.jinja2', context)


def stats_view(request):
    tasting = TastingSession.objects.first()
    checkins = tasting.checkin_set.all()
    beers = tasting.beers.all()

    context = {
        'tasting': tasting,
        'checkins': checkins,
        'beers': beers
    }

    return render_to_response('stats_view.jinja2', context)
