# Generated by Django 4.1.4 on 2023-01-30 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventHandler', '0002_sportsmansporttypeevent_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport_type_in_sport_object',
            name='count_inventory',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]