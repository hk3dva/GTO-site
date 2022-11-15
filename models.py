# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Compound(models.Model):
    athlets = models.IntegerField()
    trainers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compound'
        unique_together = (('id', 'athlets', 'trainers'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type_sport = models.ForeignKey('TypeSport', models.DO_NOTHING)

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
