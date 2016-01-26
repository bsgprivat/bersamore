from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


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
                return HttpResponseRedirect('/tasting/profile/')
    return render_to_response('index.html', context_instance=RequestContext(request))


def logout_usr(request):
    logout(request)
    return HttpResponseRedirect('/')
