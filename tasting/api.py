from django.http import HttpResponse

__author__ = 'steffe'
import requests

class Untappd(object):
    def __init__(self, client_id=None, client_secret=None, access_token=None, redirect_url=None,):
        pass


def get_systembolaget_cookies(request, sbid=None, sbpwd=None):
    get_url = u"https://www.systembolaget.se/"
    r_get = requests.post(get_url, cookies={'IsAgeVerified': '1'})
    cookies = r_get.cookies

    print cookies
    for k, v in cookies.items():
        print k, v

    #post_cookies = cookies.__dict__['_cookies']['www.systembolaget.se']['/'].items()
    #post_url = u"https://www.systembolaget.se/api/user/authenticate"

    payload = {
        'Username': sbid,
        'Password': sbpwd,
    }
    #print '-------------------------------------------------'
    #print request.COOKIES
    #print '-------------------------------------------------'

    return HttpResponse(request.COOKIES)

