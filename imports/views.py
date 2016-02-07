from datetime import datetime
from django.shortcuts import render
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
                    ib.thumb_image_url = thumb_image_url
                    changed = True
                if ib.available != available:
                    ib.available = available
                    changed = True

                if changed:
                    ib.latest_update = timezone.now()
                    ib.save()
    return u'Done'

