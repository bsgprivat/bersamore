from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = u'It is now %s' % now
    return HttpResponse(html)
