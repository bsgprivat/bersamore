from django.db import models


SOURCES = (
    (0, u'Systembolaget'),
    (1, u'Untappd'),
    (2, u'Boxbeers'),
    (3, u'Ratebeer'),
    (4, u'BeerAdvocate'),
)


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
    #, limit_choices_to={})
    hops = models.ManyToManyField(Hops, blank=True)
    style = models.ForeignKey(Style, null=True, blank=True)
    abv = models.FloatField(default=0.0)
    ibu = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    sysbol_url = models.URLField(help_text=u'systembolaget url', blank=True)

    class Meta:
        unique_together = ('name', 'brewery')

    def __unicode__(self):
        return u'%s %s - %s' % (self.brewery.name, self.name, self.style)


class ForeignID(models.Model):
    beer = models.ForeignKey(Beer)
    u_id = models.CharField(max_length=255)
    source = models.IntegerField(choices=SOURCES)

    class Meta:
        unique_together = ('beer', 'source')


class UploadedUntappdCSV(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to=u'static/files/uploads/csv')

    def __unicode__(self):
        return u'%s %s - %s' % (self.csv_file, self.name, self.date)
