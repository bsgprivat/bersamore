from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.code)


class Brewery(models.Model):
    name = models.CharField(max_length=512)
    country = models.ForeignKey(Country, blank=True, null=True)
    url = models.URLField(help_text=u'Brewery site url', blank=True)

    def __unicode__(self):
        return u'%s' % self.name


class Hops(models.Model):
    name = models.CharField(max_length=512)
    country = models.ForeignKey(Country, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.country) 

    class Meta:
        verbose_name_plural = u"hops"


class Style(models.Model):
    name = models.CharField(max_length=512)

    def __unicode__(self):
        return u'%s' % self.name


class Beer(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(null=True, blank=True, upload_to=u'static/images/uploads/beers/',
                              default=u'static/images/uploads/beers/emptybeer.jpg')
    brewery = models.ForeignKey(Brewery, blank=True, null=True)
    collabs = models.ManyToManyField(Brewery, related_name=u'collabs', blank=True, help_text=u'Collaborating breweries')
    hops = models.ManyToManyField(Hops, blank=True)
    style = models.ForeignKey(Style, null=True, blank=True)
    abv = models.FloatField(default=0.0)
    ibu = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)

#    sysbol_url = models.URLField(help_text=u'systembolaget url', blank=True)
    sysbol_id = models.IntegerField(null=True, blank=True, help_text=u'aka "varunummer", used to build urls with')
    sysbol_cart_id = models.IntegerField(null=True, blank=True, help_text=u'aka "nr", used to build carts')
    untappd_id = models.IntegerField(null=True, blank=True, help_text=u'Untappds unique Beer ID')

    class Meta:
        unique_together = ('name', 'brewery')

    def build_sysbol_url(self):
        if self.sysbol_id:
            return u'https://www.systembolaget.se/%s' % self.sysbol_id
        else:
            return None

    def __unicode__(self):
        return u'%s %s - %s' % (self.brewery.name, self.name, self.style)


class UploadedUntappdCSV(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to=u'static/files/uploads/csv')

    def __unicode__(self):
        return u'%s %s - %s' % (self.csv_file, self.name, self.date)
