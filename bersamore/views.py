from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response


def current_datetime(request):
    now = datetime.datetime.now()
    html = u'It is now %s' % now
    return render_to_response('index.html', locals())
