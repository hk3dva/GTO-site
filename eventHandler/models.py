from django.db import models
from django.contrib.auth.models import Group, User

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    birthday_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user', blank=True, null=True)
    place_employment = models.CharField(max_length=1000, blank=True, null=True)
    gto_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

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
    max_age = models.IntegerField(blank=True, null=True, default=120)
    min_age = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, choices=choice, default = 0)
    owner = models.ForeignKey(User, models.DO_NOTHING, db_column='owner')
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
    class Meta:
        managed = True
        db_table = 'sport_object'

    def __str__(self):
        return f'{self.name} {self.address}'

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

    class Meta:
        managed = True
        db_table = 'sport_type'

    def __str__(self):
        return f'{self.name}'

class SportTypeEvent(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    sportsmans = models.ManyToManyField(User, through='SportsmanSportTypeEvent', related_name='sportsmans', null=True)
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
    team = models.OneToOneField('Team', models.DO_NOTHING)
    sportsman = models.ForeignKey(User, models.DO_NOTHING, db_column='sportsman')
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