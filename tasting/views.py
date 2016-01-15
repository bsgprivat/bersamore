from __future__ import division
import random
from django.shortcuts import render, render_to_response, redirect
from cellar.models import Beer
from tasting.models import Checkin, TastingSession


def checkin_view(request):
    checkin = None
    tasting = None
    beer = None
    error = u''
    usr = request.user
    if 'tasting' in request.GET:
        try:
            t_id = int(request.GET['tasting'])
            tasting = TastingSession.objects.get(pk=t_id)
            beers = tasting.beers.all()
            if 'beer' in request.GET:
                print tasting
                print beers
                beer_id = int(request.GET['beer'])
                beer = Beer.objects.get(pk=beer_id)
        except:
            error = u'Noo tastingsession?'

        print '----------------------'
        print Checkin.objects.all()
        print tasting
        print tasting.__class__
        print beer
        print beer.__class__
        print '----------------------'
        checkin = Checkin.objects.get(tasting=tasting, beer=beer, taster=usr.taster)
        print checkin


    else:
        return redirect('/profile')


    context = {
        'error': error,
        'beer': beer,
        'usr': usr,
        'checkin': checkin,
        'tasting': tasting
    }

    return render_to_response('checkin.html', context)


def checkin_overview(request):
    tasting = TastingSession.objects.first()
    checkins = tasting.checkin_set.all()
    beers = tasting.beers.all()
    chosen_beer = None
    show_stats = False
    avg_looks = 0
    avg_smell = 0
    avg_taste = 0
    avg_overall = 0
    random_comments = None

    print request.GET

    if 'active_beer' in request.GET:
        active_beer = int(request.GET['active_beer'])
        if active_beer in [beer.pk for beer in beers]:
            chosen_beer = beers.get(pk=active_beer)
        if 'show_stats' in request.GET:
            show_stats = True
            filtered_checkins = checkins.filter(beer__pk=active_beer)
            list_of_comments = []
            aggregated_looks = 0
            aggregated_smell = 0
            aggregated_taste = 0
            aggregated_overall = 0

            for checkin in filtered_checkins:
                print checkin.taster, checkin.looks, checkin.smell, checkin.taste, checkin.overall, checkin.description
                aggregated_looks += checkin.looks
                aggregated_smell += checkin.smell
                aggregated_taste += checkin.taste
                aggregated_overall += checkin.overall
                if checkin.description:
                    list_of_comments.append(
                        checkin.description
                    )
            avg_looks = aggregated_looks/len(filtered_checkins) if aggregated_looks else u'No votes'
            avg_smell = aggregated_smell/len(filtered_checkins) if aggregated_smell else u'No votes'
            avg_taste = aggregated_taste/len(filtered_checkins) if aggregated_taste else u'No votes'
            avg_overall = aggregated_overall/len(filtered_checkins) if aggregated_overall else u'No votes'

            if list_of_comments:
                get_i = random.randint(0, len(filtered_checkins)-1)
                random_comments = list_of_comments[get_i]

    context = {
        'tasting': tasting,
        'checkins': checkins,
        'beers': beers,
        'beer': chosen_beer,
        'show_stats': show_stats,
        'avg_looks': avg_looks,
        'avg_smell': avg_smell,
        'avg_taste': avg_taste,
        'avg_overall': avg_overall,
        'random_comments': random_comments
    }

    return render_to_response('checkin_overview.html', context)


def stats_view(request):
    tasting = TastingSession.objects.first()
    checkins = tasting.checkin_set.all()
    beers = tasting.beers.all()

    context = {
        'tasting': tasting,
        'checkins': checkins,
        'beers': beers
    }

    return render_to_response('stats_view.html', context)
