# Generated by Django 5.1.2 on 2024-10-18 00:15

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_drill_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='difficulty',
            field=banjo.models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='drill',
            name='level',
            field=banjo.models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='drill',
            name='tip',
            field=banjo.models.StringField(default=''),
        ),
    ]