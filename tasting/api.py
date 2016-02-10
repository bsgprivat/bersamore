from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

__author__ = 'steffe'

from django.http import HttpResponse
from django.conf import settings

import requests


# THE HOLY GRAIL!?
# http://systembevakningsagenten.se/api/

#LOGIN/get code:
#https://untappd.com/oauth/authenticate/?client_id=D593BE394FD29B7FE11D0672D89C959D0C3D7251&response_type=code&redirect_url=http://bsg.ddns.net/api/callback/

#AUTH
#https://untappd.com/oauth/authorize/?client_id=D593BE394FD29B7FE11D0672D89C959D0C3D7251&client_secret=0CB28A694B39E2456E8A85B5EA902E7A6FB019FB&response_type=code&redirect_url=http://bsg.ddns.net/api/callback/&code=CODE

AUTH_ENDPOINT = 'https://untappd.com/oauth/authenticate'
TOKEN_ENDPOINT = 'https://untappd.com/oauth/authorize/'
API_ENDPOINT = 'https://api.untappd.com/v4'

#class Untappd(object):
#    def __init__(self, client_id=None, client_secret=None, access_token=None, redirect_url=None,):
 #       pass


def get_systembolaget_cookies(request, sbid=None, sbpwd=None):
    get_url = u"https://www.systembolaget.se/mina-sidor/?login=1"
    r_get = requests.get(get_url)
    cookies = r_get.cookies
    cookies['IsAgeVerified'] = '1'
    print cookies
    for k, v in cookies.items():
        print k, v

    # for k,v in r_post.cookies.items():
    #     print k,v
    #
    # rr_post = requests.post(get_url, cookies=p_cookies)
    #
    # print rr_post.cookies

    #post_cookies = cookies.__dict__['_cookies']['www.systembolaget.se']['/'].items()
    payload = {
        'Username': '',
        'Password': '',
    }

    post_url = u"https://www.systembolaget.se/api/user/authenticate"
    r_post = requests.post(post_url, cookies=cookies, data=payload)

    print r_post
    print r_post.cookies

    return HttpResponse(r_post.text)


def untappd_callback(request):
    if 'code' in request.GET:
        url = u'https://untappd.com/oauth/authorize/'
        client_id = settings.UNTAPPD_CLIENTID
        client_secret = settings.UNTAPPD_CLIENTSECRET
        redirect_url = settings.UNTAPPD_REDIRECT_URL
        code = request.GET[u'code']
        args = u'?client_id=%s&client_secret=%s&response_type=code&redirect_url=%s&code=%s' % (
            client_id, client_secret, redirect_url, code
        )

        r = requests.get(url+args)
        try:
            if 'response' in r.json():
                resp = r.json()['response']
                tok = resp['access_token']
                info_url = u'https://api.untappd.com/v4/user/info/?access_token=%s' % tok
                r2 = requests.get(info_url)
                untappd_name = r2.json()['response']['user']['user_name']
                return HttpResponse(u'HEJ (untappd:id) %s' % untappd_name)
        except Exception as e:
            return HttpResponse(e)

        return HttpResponse(r.json()['response'])
    else:
        return HttpResponse('BAAAD')


@login_required(login_url='/')
def login_untappd(request, code=None):
    code = untappd_callback()
    url = u'https://untappd.com/oauth/authorize/'
    client_id=settings.UNTAPPD_CLIENTID
    client_secret=settings.UNTAPPD_CLIENTSECRET
    redirect_url = settings.UNTAPPD_REDIRECT_URL
    code = request.GET[u'code']
    args = u'?client_id=%s&client_secret=%s&response_type=code&redirect_url=%s&code=%s' % (
        client_id, client_secret, redirect_url, code
    )

    r = requests.get(url+args)

