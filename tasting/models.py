from django.contrib.auth.models import User
from django.db import models
from cellar.models import Beer, Brewery, Style
from django.core.validators import MinValueValidator, MaxValueValidator


class Taster(models.Model):
    user = models.OneToOneField(User)
    fav_beers = models.ManyToManyField(Beer, blank=True)
    fav_breweries = models.ManyToManyField(Brewery, blank=True)
    fav_styles = models.ManyToManyField(Style, blank=True)
    friends = models.ManyToManyField('tasting.Taster', related_name=u'tasterfriends')

    def __unicode__(self):
        if self.user.last_name:
            return u'%s %s' % (self.user.first_name, self.user.last_name[0])
        else:
            return u'%s' % self.user.email


class TastingSession(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date = models.DateTimeField()
    tasters = models.ManyToManyField(Taster)
    beers = models.ManyToManyField(Beer, blank=True, through='tasting.TastingBeers')
    finished = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.date.strftime('%y-%m-%d %H:%M'))


class TastingBeers(models.Model):
    beer = models.ForeignKey(Beer)
    tasting = models.ForeignKey(TastingSession)

    class Meta:
        unique_together = ('beer', 'tasting')


class Checkin(models.Model):
    taster = models.ForeignKey(Taster)
    beer = models.ForeignKey(Beer)
    tasting = models.ForeignKey(TastingSession)

    looks = models.IntegerField(
        blank=True, null=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    nose = models.IntegerField(
        blank=True, null=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    taste = models.IntegerField(
        blank=True, null=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    overall = models.IntegerField(
        blank=True, null=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    notes = models.TextField(blank=True, null=True, max_length=300)

    def __unicode__(self):
        return u'%s %s %s (%s)' % (self.taster, self.beer, self.tasting, self.overall)
