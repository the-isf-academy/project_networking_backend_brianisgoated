# Generated by Django 5.1.2 on 2024-10-23 00:39

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_drill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='difficulty',
            field=banjo.models.IntegerField(default=0),
        ),
    ]