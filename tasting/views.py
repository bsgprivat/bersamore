from __future__ import division
import random
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as conf_settings
from cellar.models import Beer
from tasting.api import test_untappd_login
from tasting.models import Checkin, TastingSession


@csrf_exempt
@login_required(login_url='/')
def checkin_view(request, beer_id=None):
    checkin = None
    checkins = None
    beer = None
    error = u''
    usr = request.user

    if beer_id:
        beer = Beer.objects.get(pk=int(beer_id))
        checkins = Checkin.objects.filter(beer=beer, taster=usr.taster)

        if request.POST:
            b_id = int(request.POST['beer'])
            beer = Beer.objects.get(pk=b_id)

            notes = request.POST['notes']
            looks = int(request.POST['looks'])
            nose = int(request.POST['nose'])
            taste = int(request.POST['taste'])
            overall = int(request.POST['overall'])

            checkin, created = Checkin.objects.get_or_create(
                beer=beer, taster=usr.taster,
            )

            checkin.looks = looks
            checkin.nose = nose
            checkin.taste = taste
            checkin.overall = overall
            checkin.notes = notes
            checkin.save()

            return redirect(u'.', b_id)
    else:
        error = u'You have to choose a beer.'

    context = {
        'error': error,
        'beer': beer,
        'usr': usr,
        'checkin': checkin,
        'checkins': checkins,
    }

    return render_to_response('checkin.html', context)


@csrf_exempt
@login_required(login_url='/')
def tasting_checkin_view(request, tasting_id=None, beer_i=None):
    checkin = None
    tasting = None
    beer = None
    prev = None
    next = None
    error = u''
    usr = request.user

    try:
        tasting = TastingSession.objects.get(pk=tasting_id)
        if usr.taster not in tasting.tasters.all():
            return HttpResponse("You are not participating in this tasting, are you?")

    except Exception as e:
        return HttpResponse(e)

    beers = tasting.ordered_beers
    beer_count = len(tasting.ordered_beers)

    if beer_i:
        beer_i = int(beer_i)
        beer = beers[beer_i-1]
        if beer_i < beer_count:
            next = beer_i + 1
        if beer_i > 1:
            prev = beer_i-1

    try:
        checkin = Checkin.objects.get(tasting=tasting, beer=beer, taster=usr.taster)
    except:
        pass

    if request.POST:
        t_id = int(request.POST['tasting'])
        b_id = int(request.POST['beer'])

        tasting = TastingSession.objects.get(pk=t_id)
        beer = Beer.objects.get(pk=b_id)
        notes = request.POST['notes']
        looks = int(request.POST['looks'])
        nose = int(request.POST['nose'])
        taste = int(request.POST['taste'])
        overall = int(request.POST['overall'])
        
        checkin, created = Checkin.objects.get_or_create(
            tasting=tasting, beer=beer, taster=usr.taster,
        )

        checkin.looks = looks
        checkin.nose = nose
        checkin.taste = taste
        checkin.overall = overall
        checkin.notes = notes
        checkin.save()

        return redirect(u'.', t_id, b_id)


    context = {
        'error': error,
        'beer': beer,
        'beer_i': beer_i,
        'beer_count': beer_count,
        'usr': usr,
        'prev': prev,
        'next': next,
        'checkin': checkin,
        'tasting': tasting
    }

    return render_to_response('tasting_checkin.html', context)


@login_required(login_url='/')
def checkin_overview(request, tasting_id=None):
    tasting = TastingSession.objects.get(pk=int(tasting_id))
    checkins = tasting.checkin_set.all()
    beers = tasting.ordered_beers
    chosen_beer = None
    show_stats = False
    avg_looks = 0
    avg_nose = 0
    avg_taste = 0
    avg_overall = 0
    count_looks = 0
    count_nose = 0
    count_taste = 0
    count_overall = 0
    random_comments = None

    if 'active_beer' in request.GET:
        active_beer = int(request.GET['active_beer'])
        if active_beer in [beer.pk for beer in beers]:
            chosen_beer = Beer.objects.get(pk=active_beer)

        if 'show_stats' in request.GET:
            show_stats = True
            filtered_checkins = checkins.filter(beer__pk=active_beer)
            list_of_comments = []
            aggregated_looks = 0
            aggregated_nose = 0
            aggregated_taste = 0
            aggregated_overall = 0

            for checkin in filtered_checkins:
                if checkin.looks:
                    aggregated_looks += checkin.looks
                    count_looks += 1
                if checkin.nose:
                    aggregated_nose += checkin.nose
                    count_nose += 1
                if checkin.taste:
                    aggregated_taste += checkin.taste
                    count_taste += 1
                if checkin.overall:
                    aggregated_overall += checkin.overall
                    count_overall += 1

                if checkin.notes:
                    list_of_comments.append(
                        checkin.notes
                    )
            avg_looks = aggregated_looks/count_looks if aggregated_looks else u'No votes'
            avg_nose = aggregated_nose/count_nose if aggregated_nose else u'No votes'
            avg_taste = aggregated_taste/count_taste if aggregated_taste else u'No votes'
            avg_overall = aggregated_overall/count_overall if aggregated_overall else u'No votes'

            if list_of_comments:
                random.shuffle(list_of_comments)
                random_comments = list_of_comments[:3]

                #TODO: stats needs to be:
                # [grade (dvs 1), number of ones for nose, ..looks, taste.. overall
                # list of lists.

    context = {
        'tasting': tasting,
        'checkins': checkins,
        'beers': beers,
        'beer': chosen_beer,
        'show_stats': show_stats,
        'avg_looks': avg_looks,
        'avg_nose': avg_nose,
        'avg_taste': avg_taste,
        'avg_overall': avg_overall,
        'random_comments': random_comments
    }

    return render_to_response('checkin_overview.html', context)


@login_required(login_url='/')
def stats_view(request, tasting_id):
    tasting = TastingSession.objects.get(pk=int(tasting_id))
    checkins = tasting.checkin_set.all().order_by('-date')
    checkin_beers_dict = {}
    best_of = []

    for checkin in checkins:
        try:
            checkin_beers_dict[checkin.beer].append(checkin.overall)
        except KeyError:
            checkin_beers_dict[checkin.beer] = [checkin.overall]

    for k, v in checkin_beers_dict.items():
        n = len(v)
        tot = 0
        for i in v:
            tot += i
        avg = tot/n
        best_of.append((avg, k))

    best_of = sorted(best_of, key=lambda best: float(best[0]))
    best_of.reverse()

    context = {
        'tasting': tasting,
        'checkins': checkins,
        'best_of': best_of,
    }
    return render_to_response('stats_view.html', context)


@login_required(login_url='/')
def profile(request):
    usr = request.user
    tastings = TastingSession.objects.filter(tasters=usr.taster)
    checkins = Checkin.objects.filter(taster=usr.taster).order_by('-date')
    admin = False
    if usr.is_superuser:
        admin = True
    client_id= conf_settings.UNTAPPD_CLIENTID
    redirect_url = conf_settings.UNTAPPD_REDIRECT_URL
    auth_url = conf_settings.UNTAPPD_AUTH_URL

    untappd_login_url = u'%s?client_id=%s&response_type=code&redirect_url=%s' % (
        auth_url, client_id, redirect_url
    )
    logged_in, u_context = test_untappd_login(usr.taster)
    latest = []

    if u_context:
        recent = u_context['recent_brews']['items']
        for r in recent:
            latest.append(
                [
                    r['beer']['beer_name'],
                    r['beer']['beer_style'],
                    r['beer']['auth_rating']
                ]
            )


    context = {
        'usr': usr,
        'tastings': tastings,
        'checkins': checkins[:10],
        'admin': admin,
        'untappd_login_url': untappd_login_url,
        'logged_in': logged_in,
        'latest': latest
    }

    return render_to_response(
        'profile.html', context
    )


@login_required(login_url='/')
def checkins(request, filters=None):
    usr = request.user
    checkins = Checkin.objects.filter(taster=usr.taster).order_by('-overall')
    all_beers = checkins.values_list('beer',flat=True).order_by('beer')

    checkin_beers_dict = {}
    top_beers = []

    for checkin in checkins:
        try:
            checkin_beers_dict[checkin.beer].append(checkin.overall)
        except KeyError:
            checkin_beers_dict[checkin.beer] = [checkin.overall]

    for k, v in checkin_beers_dict.items():
        n = len(v)
        tot = 0
        for i in v:
            tot += i
        avg = tot/n
        top_beers.append((avg, k))

    top_beers = sorted(top_beers, key=lambda best: float(best[0]))
    top_beers.reverse()
    print top_beers
    context = {
        'usr': usr,
        'checkins': checkins,
        'count': checkins.count(),
        'all_beers': all_beers,
        'beers': top_beers,
        'filters': filters,
    }

    return render_to_response(
        'checkins.html', context
    )

@login_required(login_url='/')
def settings(request):
    usr = request.user

    client_id = conf_settings.UNTAPPD_CLIENTID
    redirect_url = conf_settings.UNTAPPD_REDIRECT_URL
    auth_url = conf_settings.UNTAPPD_AUTH_URL
    untappd_login_url = u'%s?client_id=%s&response_type=code&redirect_url=%s' % (
        auth_url, client_id, redirect_url
    )

    if request.POST:
        print request.POST

    context = {
        'usr': usr,
        'untappd_login_url': untappd_login_url
    }

    return render_to_response(
        'settings.html', context
    )


@login_required(login_url='/')
def baseview(request, tasting_id=None):
    usr = request.user
    tastings = TastingSession.objects.all()
    tasting = None
    now = datetime.datetime.now()
    can_start = False
    if tasting_id:
        tasting = tastings.get(pk=int(tasting_id))
        if tasting.date.replace(tzinfo=None) < now.replace(tzinfo=None):
            can_start = True
    else:
        return redirect('/profile/')

    context = {
        'usr': usr,
        'now': now,
        'tasting': tasting,
        'tastings': tastings,
        'can_start': can_start
    }

    return render_to_response(
        'tasting_base.html', context
    )

@csrf_exempt
@login_required(login_url='/')
def tastestats(request, tasting_id=None):
    tasting = TastingSession.objects.get(pk=int(tasting_id))
    usr = request.user
    checkins = tasting.checkin_set.filter(taster=usr.taster)

    if request.POST:
        ids_string = u''
        if u'sys_id' in request.POST:
            for i in request.POST.getlist(u'sys_id'):
                ids_string += u'%s:1,' % i

        return redirect(
            u'https://www.systembolaget.se/dryckeslista?items=%s' % ids_string[:-1]
        )

    context ={
        'usr': usr,
        'tasting': tasting,
        'checkins': checkins
    }

    return render_to_response('tastestats.html', context)
