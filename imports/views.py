#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, render_to_response
from django.utils import timezone
import requests
from imports.models import ImportedBeer


def scrape_me():
    nget = requests.get('http://www.systembolaget.se/api/productsearch/search?subcategory=%C3%96l')
    nums = nget.json()['Metadata']['DocCount']

    pnum = nums//10+2
    pages = [page for page in range(0, pnum)]
    if pages:
        for page in pages:
            print page
            start_url = u'http://www.systembolaget.se/api/productsearch/search?subcategory=%C3%96l&sortfield=SellStartDate&sortdirection=Descending&site=all&fullassortment=1&nofilters=1&page='
            start_url += u'%s' % page
            r = requests.get(start_url)
            js = r.json()
            prods = js['ProductSearchResults']

            for p in prods:
                name_plus = u''
                if p['ProductNameThin']:
                    name_plus = u' - ' + p['ProductNameThin']
                name = p['ProductNameBold'] + name_plus
                url = u'https://www.systembolaget.se' + u'%s' % p['ProductUrl']
                sysbol_id = p['ProductNumber'][:-2]
                sysbol_cart_id = p['ProductNumber']
                sysbol_price = float(p['PriceText'].replace(',', '.'))
                thumb_image_url = None
                available = True
                size = p['VolumeText']
                realease = p['SellStartText']
                if len(realease) > 11:
                    realease = realease[10:]
                if p['Availability']:
                    available = False

                if p['Thumbnail']['ImageUrl']:
                    thumb_image_url = u'https:' + p['Thumbnail']['ImageUrl']
                ib, created = ImportedBeer.objects.get_or_create(
                                sysbol_id=sysbol_id,
                                sysbol_cart_id=sysbol_cart_id
                )
                changed = False
                if ib.name != name:
                    ib.name = name
                    changed = True
                if ib.url != url:
                    ib.url = url
                    changed = True
                if ib.size != size:
                    ib.size = size
                    changed = True
                if ib.sysbol_price != sysbol_price:
                    ib.sysbol_price = sysbol_price
                    ib.sysbol_price_checked = timezone.now()
                    changed = True

                if ib.thumb_image_url != thumb_image_url:
                    if thumb_image_url:
                        ib.thumb_image_url = thumb_image_url
                        changed = True
                if ib.available != available:
                    ib.available = available
                    changed = True

                if ib.realease != realease and realease:
                    ib.realease = realease
                    changed = True

                if changed:
                    ib.latest_update = timezone.now()
                    ib.save()
    return u'Done'


def list_imports(request):
    print request.GET
    if request.user.is_superuser:
        available = False
        pics = False
        size = False
        price_from = 0
        price_to = 0
        created_from = False
        created_to = False
        updated_from = False
        updated_to = False
        filters = True

        imports = ImportedBeer.objects.all().order_by('latest_update')
        size_list = list(set(imports.values_list('size', flat=True)))
        size_list.sort()

        if 'available' in request.GET:
            available = request.GET['available']
            if available:
                imports = imports.filter(available=True)

        if 'size' in request.GET:
            size = request.GET['size']
            if size:
                imports = imports.filter(size=size)

        if 'price_from' in request.GET:
            price_from = request.GET['price_from']
            if price_from:
                price_from = float(price_from)
                imports = imports.filter(sysbol_price__gte=price_from)

        if 'price_to' in request.GET:
            price_to = request.GET['price_to']
            if price_to:
                price_to = float(price_to)
                imports = imports.filter(sysbol_price__gte=price_to)

        if 'created_from' in request.GET:
            created_from = request.GET['created_from']
            if created_from:
                imports = imports.filter(created__gte=created_from)

        if 'created_to' in request.GET:
            created_to = request.GET['created_to']
            if created_to:
                imports = imports.filter(created__lte=created_to)

        if 'updated_from' in request.GET:
            updated_from = request.GET['updated_from']
            if updated_from:
                imports = imports.filter(latest_update__gte=updated_from)

        if 'updated_to' in request.GET:
            updated_to = request.GET['updated_to']
            if updated_to:
                imports = imports.filter(latest_update__lte=updated_to)

        if 'pics' in request.GET:
            pics = request.GET['pics']
            if pics:
                imports = imports.filter(thumb_image_url__isnull=False)

        if not any([available,pics,size,price_from,price_to,
                    created_to,created_from,updated_from,updated_to]):
            filters = None

    return render_to_response('list.html', locals())
