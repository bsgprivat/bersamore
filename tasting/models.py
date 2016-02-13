from django.contrib.auth.models import User
from django.db import models
from cellar.models import Beer, Brewery, Style
from django.core.validators import MinValueValidator, MaxValueValidator

INVITATION_STATUSES = (
    (0, u'Invited'),
    (1, u'Accepted'),
    (2, u'Declined')
)


class Login(models.Model):
    usr = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add=True)


class Taster(models.Model):
    user = models.OneToOneField(User)
    display_email = models.BooleanField(default=False)
    receieve_email = models.BooleanField(default=True)
    public = models.BooleanField(default=False)
    allow_contacs = models.BooleanField(default=True)
    fav_beers = models.ManyToManyField(Beer, blank=True)
    fav_breweries = models.ManyToManyField(Brewery, blank=True)
    fav_styles = models.ManyToManyField(Style, blank=True)
    friends = models.ManyToManyField('tasting.Taster', related_name=u'tasterfriends', blank=True)
    # stores in area?
    # http://systembevakningsagenten.se/api/json/1.0/inventoryForStore.json?id=1001

    sysbol_id = models.EmailField(
        null=True, blank=True,
        help_text=u'Used to connect against your systembolaget account'
    )
    allow_sysbol_fetch = models.BooleanField(
        default=False,
        help_text=u'Allow BMS to fetch your orderlists'
    )
    untappd_id = models.CharField(max_length=512, blank=True, null=True)
    untappd_token = models.CharField(max_length=512, blank=True, null=True)


    @property
    def beers(self):
        return self.fav_beers.all()

    @property
    def breweries(self):
        return self.fav_breweries.all()

    @property
    def styles(self):
        return self.fav_styles.all()

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return u'%s %s' % (self.user.first_name, self.user.last_name[0])
        if self.user.username:
            return self.user.username
        else:
            return u'%s' % self.user.email


class TastingSession(models.Model):
    name = models.CharField(max_length=256)
    administrators = models.ManyToManyField(Taster, related_name=u'tasting_admin')
    description = models.TextField()
    date = models.DateTimeField()
    tasters = models.ManyToManyField(Taster)
    beers = models.ManyToManyField(Beer, blank=True, through='tasting.TastingBeers')
    finished = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.date.strftime('%y-%m-%d %H:%M'))

    @property
    def ordered_beers(self):
        return [beer.beer for beer in self.tastingbeers_set.order_by(u'position')]

    def participating_tasters(self):
        return [t for t in self.tastinginvitation_set.all() if t.status == INVITATION_STATUSES[1]]


class TastingBeers(models.Model):
    beer = models.ForeignKey(Beer)
    tasting = models.ForeignKey(TastingSession)
    position = models.PositiveIntegerField(default=0)
    # TODO
    # description = models.TextField(blank=True, null=True, help_text=u'Overrides description from beer.')

    class Meta:
        unique_together = (u'beer', u'tasting')
        ordering = [u'position', ]


class TastingInvitation(models.Model):
    tasting = models.ForeignKey(TastingSession)
    taster = models.ForeignKey(Taster)
    status = models.IntegerField(choices=INVITATION_STATUSES, default=0)

    class Meta:
        unique_together = ('taster', 'tasting')


class Checkin(models.Model):
    taster = models.ForeignKey(Taster)
    beer = models.ForeignKey(Beer)
    date = models.DateTimeField(auto_now_add=True)
    tasting = models.ForeignKey(TastingSession, blank=True, null=True)
    from_untappd = models.BooleanField(default=False)
    pushed_to_untapppd =models.BooleanField(default=False)
    untappd_id = models.IntegerField(null=True, blank=True)

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
