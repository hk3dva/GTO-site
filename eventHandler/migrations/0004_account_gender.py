# Generated by Django 4.1.4 on 2023-01-31 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventHandler', '0003_sport_type_in_sport_object_count_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Женщина'), (1, 'Мужчина')], default=2, null=True),
        ),
    ]
