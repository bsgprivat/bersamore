from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2)
    flag = models.ImageField(
        null=True, blank=True,
        upload_to=u'static/images/uploads/flags/',
        help_text=u'Use "country-code.png"'
    )

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.code)


class Brewery(models.Model):
    name = models.CharField(max_length=512)
    country = models.ForeignKey(Country, blank=True, null=True)
    url = models.URLField(help_text=u'Brewery site url')
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
    image = models.ImageField(null=True, blank=True, upload_to=u'static/images/uploads/beers/')
    brewery = models.ForeignKey(Brewery, blank=True, null=True)
    collabs = models.ManyToManyField(Brewery, related_name=u'collabs', blank=True, help_text=u'Collaborating breweries')
    #, limit_choices_to={})
    hops = models.ManyToManyField(Hops, blank=True)
    style = models.ForeignKey(Style, null=True, blank=True)
    abv = models.FloatField(default=0.0)
    ibu = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    sysbol_url = models.URLField(help_text=u'systembolaget url')

    def __unicode__(self):
        return u'%s %s - %s' % (self.brewery.name, self.name, self.style)
