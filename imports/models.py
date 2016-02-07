from django.db import models
import requests
from bs4 import BeautifulSoup

class ImportedBeer(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True, help_text=u'Name of beer')
    image_url = models.CharField(max_length=512, blank=True, null=True, help_text=u'image url',
                              default=u'static/images/uploads/beers/emptybeer.jpg')
    thumb_image_url = models.CharField(max_length=512, blank=True, null=True, help_text=u'image url',
                              default=u'static/images/uploads/beers/emptybeer.jpg')
    brewery = models.CharField(max_length=512, blank=True, null=True, help_text=u'Name of Brewery')

    collabs = models.CharField(max_length=512, blank=True, null=True, help_text=u'Collaborating breweries')
    abv = models.FloatField(default=0.0)
    ibu = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    ean = models.IntegerField(null=True, blank=True)

    sysbol_id = models.IntegerField(null=True, blank=True, help_text=u'aka "varunummer", used to build urls with')
    sysbol_cart_id = models.IntegerField(null=True, blank=True, help_text=u'aka "nr", used to build carts')
    sysbol_price = models.FloatField(blank=True, null=True)
    sysbol_price_checked_date = models.DateTimeField(blank=True, null=True)
    cant_be_ordered = models.BooleanField(default=False)
    batch_size = models.IntegerField(null=True,blank=True, help_text=u'Only sold in batches')
    url = models.CharField(max_length=512, blank=True, null=True, help_text=u'url to product')

    def update(self):
        if self.url:
            r = requests.get(self.url)
            fetch = BeautifulSoup(r.text)
            price = fetch.find('li', {"class": 'price'})
            name = fetch.find('li', {"class": 'subtitle'})
            brewery = fetch.find('li', {"class": 'name'})

            print price
            print name
            print brewery