from django.db import models
import requests
from bs4 import BeautifulSoup

class ImportedBeer(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True, help_text=u'Name of beer')
    image_url = models.CharField(max_length=512, blank=True, null=True, help_text=u'image url')
    thumb_image_url = models.CharField(
        max_length=512, blank=True, null=True, help_text=u'image url',
        default=u'https//static.systembolaget.se/content/assets/images/products/thumbnail_noimage.png'
    )
    brewery = models.CharField(max_length=512, blank=True, null=True, help_text=u'Name of Brewery')
    realease = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    latest_update = models.DateTimeField(null=True, blank=True)

    collabs = models.CharField(max_length=512, blank=True, null=True, help_text=u'Collaborating breweries')
    abv = models.FloatField(default=0.0)
    ibu = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=64, null=True, blank=True)
    ean = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=128, blank=True, null=True)

    sysbol_id = models.IntegerField(null=True, blank=True, help_text=u'aka "varunummer", used to build urls with')
    sysbol_cart_id = models.IntegerField(null=True, blank=True, help_text=u'aka "nr", used to build carts')
    sysbol_price = models.FloatField(blank=True, null=True)
    sysbol_price_checked_date = models.DateTimeField(blank=True, null=True)
    cant_be_ordered = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    batch_size = models.IntegerField(null=True, blank=True, help_text=u'Only sold in batches')
    url = models.CharField(max_length=512, blank=True, null=True, help_text=u'url to product')

    def update(self):
        if self.url:
            print self.url
            r = requests.get(self.url)
            print r.text
            fetch = BeautifulSoup(r.text, 'html.parser')
            price = fetch.find('li', {"class": 'price'})
            name = fetch.find('li', {"class": 'subtitle'})
            brewery = fetch.find('li', {"class": 'name'})

            print price
            print price.string
            print name
            print name.string
            print brewery
            print brewery.string

    def __unicode__(self):
        return u'%s' % self.name