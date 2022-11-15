from django.db import models

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
    photo = models.TextField(blank=True, null=True)
    place_employment = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'

class Compound(models.Model):
    athlets = models.ManyToManyField(AuthUser, related_name='athlets_set', through="UserCompound")
    trainers = models.ManyToManyField(AuthUser, related_name='trainers_set', through="TrainterCompound")

    class Meta:
        managed = False
        db_table = 'compound'
        # unique_together = (('id', 'athlets', 'trainers'),)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type_sport = models.ForeignKey('TypeSport', models.DO_NOTHING)
    teams = models.ManyToManyField('Team', related_name='teams_set', through="TeamHasEvent")

    class Meta:
        managed = False
        db_table = 'event'
        unique_together = (('event_id', 'type_sport'),)

    def get_absolute_url(self):
        return '/event'

    def __str__(self):
        return f"{self.name}, {self.date}"


class Organization(models.Model):
    orhanization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'

    def __str__(self):
        return f'{self.name}'


class SportObject(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    place = models.CharField(max_length=1000, blank=True, null=True)
    type_sport = models.ForeignKey('TypeSport', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(Organization, models.DO_NOTHING, db_column='owner')

    class Meta:
        managed = False
        db_table = 'sport_object'
        unique_together = (('id', 'owner'),)

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    compound = models.ForeignKey(Compound, models.DO_NOTHING, db_column='compound')

    class Meta:
        managed = False
        db_table = 'team'
        unique_together = (('team_id', 'compound'),)

    def __str__(self):
        return f'{self.name}'


class TeamHasEvent(models.Model):
    team_team = models.OneToOneField(Team, models.DO_NOTHING, primary_key=True)
    event_event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_has_event'
        unique_together = (('team_team', 'event_event'), ('team_team', 'event_event'),)


class TrainterCompound(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    compound = models.OneToOneField(Compound, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trainter_compound'
        unique_together = (('user', 'compound'),)


class TypeSport(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_sport'

    def __str__(self):
        return f'{self.name}'


class UserCompound(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    compound = models.OneToOneField(Compound, models.DO_NOTHING, db_column='compound')

    class Meta:
        managed = False
        db_table = 'user_compound'
        unique_together = (('user', 'compound'),)


class UserEvent(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_event'
        unique_together = (('user', 'event'),)


class UserResult(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    result = models.CharField(max_length=45, blank=True, null=True)
    sport_type = models.ForeignKey(TypeSport, models.DO_NOTHING, db_column='sport_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_result'
