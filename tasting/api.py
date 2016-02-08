from django.http import HttpResponse

__author__ = 'steffe'
import requests


# THE HOLY GRAIL!?
# http://systembevakningsagenten.se/api/

class Untappd(object):
    def __init__(self, client_id=None, client_secret=None, access_token=None, redirect_url=None,):
        pass


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
    # print r_post.headers
    # print r_post.history
    # print r_post.raw
    # print r_post.request
    # print r_post._content
    # print r_post.text
    # print r_post.json()

    return HttpResponse(r_post.text)


def untappd_callback(request):
    print request.GET
    return HttpResponse('HEPP')