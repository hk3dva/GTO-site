from django.db import models
from django.contrib.auth.models import Group, User, AbstractUser
from django.conf import settings

class City(models.Model):
    name = models.CharField(max_length=1000)
    class Meta:
        managed = True
        db_table = 'City'
    def __str__(self):
        return f'{self.name}'

class Organization(models.Model):
    name = models.CharField(max_length=1000)
    class Meta:
        managed = True
        db_table = 'Organization'
    def __str__(self):
        return f'{self.name}'

class Account(AbstractUser):
    birthday_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user', blank=True, null=True)
    gto_id = models.IntegerField(blank=True, null=True, unique=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', null=True, blank=True,)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization', null=True, blank=True)
    class Meta:
        managed = True
        db_table = 'Account'

    def get_absolute_url(self):
        return '/event'

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'


class Event(models.Model):
    choice = (
        (0, 'Планируется'),
        (1, 'Проводится'),
        (2, 'Подводятся итоги'),
        (3, 'Завершенно'),
    )
    age_max = models.IntegerField(blank=True, null=True, default=120)
    age_min = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, choices=choice, default = 0)
    owner = models.ForeignKey(Account, models.DO_NOTHING, db_column='owner')
    settings = models.ManyToManyField('SportTypeEvent', through='SportTypeEventHasEvent', related_name='settings')
    photo = models.ImageField(upload_to='event', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'event'
        unique_together = (('id', 'owner'),)

    def get_absolute_url(self):
        return '/event'

    def __str__(self):
        return f"{self.name}"

class SportObject(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    photo = models.ImageField(upload_to='sportObject', blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    sport_type = models.ManyToManyField('SportType', through='Sport_type_in_sport_object', related_name='sport_in_object', null=True)

    class Meta:
        managed = True
        db_table = 'sport_object'

    def __str__(self):
        return f'{self.name} {self.address}'

class Sport_type_in_sport_object(models.Model):
    sport_object = models.OneToOneField(SportObject, models.DO_NOTHING, primary_key=True)
    count_inventory = models.IntegerField(blank=True, null=True, default=0)
    sport_type = models.ForeignKey('SportType', models.DO_NOTHING)
    class Meta:
        managed = True
        db_table = 'Sport_type_in_sport_object'
        unique_together = (('sport_object', 'sport_type'),)

class Standards(models.Model):
    sport_type = models.ForeignKey('SportType', models.DO_NOTHING)
    time = models.TimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True )

    def __str__(self):
        return f'{self.sport_type.name} {self.points}'
    class Meta:
        managed = True
        db_table = 'Standards'
        unique_together = (('sport_type', 'points'),)

class SportType(models.Model):
    choice = (
        (0, 'Да'),
        (1, 'Нет')
    )
    choice_gender =(
        (0, 'только Женщины'),
        (1, 'только Мужчины'),
        (2, 'Все')
    )
    name = models.CharField(max_length=45, blank=True, null=True)
    custom = models.IntegerField(blank=True, null=True, choices=choice, default=1)
    for_who = models.IntegerField(blank=True, null=True, choices=choice_gender, default=2)
    teamable = models.IntegerField(blank=True, null=True, choices=choice, default=1)
    age_max = models.IntegerField(blank=True, null=True, default=120)
    age_min = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = True
        db_table = 'sport_type'

    def __str__(self):
        return f'{self.name}'

class SportTypeEvent(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    sportsmans = models.ManyToManyField(Account, through='SportsmanSportTypeEvent', related_name='sportsmans', null=True, blank=True)
    sport_type = models.ForeignKey(SportType, models.DO_NOTHING)
    sport_object = models.ForeignKey(SportObject, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sport_type_event'
        unique_together = (('id', 'sport_type', 'sport_object'),)

    def __str__(self):
        return f'{self.date} {self.time} {self.sport_object} {self.sport_type}'


class SportTypeEventHasEvent(models.Model):
    sport_type_event = models.OneToOneField(SportTypeEvent, models.DO_NOTHING, primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sport_type_event_has_event'
        unique_together = (('sport_type_event', 'event'),)


class SportsmanSportTypeEvent(models.Model):
    team = models.OneToOneField('Team', models.DO_NOTHING, blank=True, null=True)
    sportsman = models.ForeignKey(Account, models.DO_NOTHING, db_column='sportsman')
    result = models.CharField(max_length=100, blank=True, null=True)
    sport_type_event = models.ForeignKey(SportTypeEvent, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sportsman_sport_type_event'
        unique_together = (('team', 'sportsman', 'sport_type_event'),)


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'team'

    def __str__(self):
        return f'{self.name}'