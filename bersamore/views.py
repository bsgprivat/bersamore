from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from cellar.models import Beer
from tasting.models import Login, Taster


@csrf_exempt
def index(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                Login.objects.create(usr=user)
                return HttpResponseRedirect('/profile/')
    return render_to_response('index.html', context_instance=RequestContext(request))


def logout_usr(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
@csrf_exempt
def search(request):
    usr = request.user.taster
    beers = Beer.objects.all()
    tasters = Taster.objects.filter(allow_contacts=True)
    beer_list = []
    more_beers = u''
    for x in range(0, 12):
        beer_list.append(beers.first())

    if request.POST:
        if u'search' in request.POST:
            q = request.POST[u'search']
            if len(q) < 2:
                beers = None
                tasters = None
                q = u'"%s" is too short, at least two characters plz.' % q

            if len(beer_list) > 10:
                beer_list = beer_list[:10]
            more_beers = u'LOAD MORE'

    return render_to_response('search_results.html', locals())

@login_required(login_url='/')
def user_browse(request):
    users = User.objects.filter(taster__allow_contacts=True).order_by('-date_joined')
    names = users.values_list('username', flat=True)
    letters = list(set([name[0].lower() for name in names]))

    letters.sort()
    if not 'letter' in request.GET:
        users = list(users)[:1]
    else:
        l = request.GET[u'letter']
        users = users.filter(username__startswith=l)

    return render_to_response('user_browse.html', locals())

@login_required(login_url='/')
def beer_browse(request):
    beers = Beer.objects.all().order_by('-name')
    names = beers.values_list('name', flat=True)
    letters = list(set([name[0].lower() for name in names]))

    letters.sort()
    if not 'letter' in request.GET:
        users = list(beers)[:1]
    else:
        l = request.GET[u'letter']
        beers = beers.filter(name__startswith=l)

    return render_to_response('beer_browse.html', locals())
