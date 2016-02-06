from django.db import models

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
    #untappd_id = m