from django.contrib.auth.models import User
from django.db import models
from cellar.models import Beer, Brewery, Style
from django.core.validators import MinValueValidator, MaxValueValidator

INVITATION_STATUSES = (
    (0, u'Invited'),
    (1, u'Accepted'),
    (2, u'Declined')
)


class County(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.name


class City(models.Model):
    name = models.CharField(max_length=256)
    county = models.ForeignKey(County)

    def __unicode__(self):
        return u'%s %s' % (
            self.name, self.county
        )


class Store(models.Model):
    store_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=256)
    city = models.ForeignKey(City)
    zip_code = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s %s' % (
            self.store_id, self.address, self.city
        )


class Login(models.Model):
    usr = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add=True)


class Taster(models.Model):
    user = models.OneToOneField(User)
    receieve_email = models.BooleanField(default=True)
    allow_contacts = models.BooleanField(default=True)
    fav_beers = models.ManyToManyField(Beer, blank=True)
    fav_breweries = models.ManyToManyField(Brewery, blank=True)
    fav_styles = models.ManyToManyField(Style, blank=True)
    friends = models.ManyToManyField('tasting.Taster', related_name=u'tasterfriends', blank=True)
    stores = models.ManyToManyField(Store, blank=True)
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

    @property
    def checkin_count(self):
        return Checkin.objects.filter(taster=self).count()

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return u'%s %s' % (self.user.first_name, self.user.last_name[0])
        if self.user.username:
            return self.user.username
        else:
            return u'%s' % self.user.email


class Friendship(models.Model):
    status = models.IntegerField(default=0, choices=INVITATION_STATUSES)
    inviter = models.ForeignKey(Taster, related_name=u'friend_inviter')
    receiver = models.ForeignKey(Taster, related_name=u'friend_receiver')
    date_created = models.DateTimeField(auto_now_add=True)
    date_accepted = models.DateTimeField(blank=True, null=True)

    def users(self):
        return Taster.objects.filter(id__in=[self.inviter.pk, self.receiver.pk])

    def friends(self, taster):
        invs = self.filter(status=1, inviter=taster).values_list('receiver', flat=True)
        recs = self.filter(status=1, receiver=taster).values_list('inviter', flat=True)
        ids = recs+invs
        friends = Taster.objects.filter(id__in=ids)
        return friends

    class Meta:
        unique_together = ('inviter', 'receiver')
        ordering = ['-date_accepted', '-date_created']

    def __unicode__(self):
        return u'%s + %s %s' % (self.inviter, self.receiver, self.get_status_display())


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

    def save(self, *args, **kwargs):
        super(Checkin, self).save(*args, **kwargs)
        beer = self.beer
        beer.recalculate()
