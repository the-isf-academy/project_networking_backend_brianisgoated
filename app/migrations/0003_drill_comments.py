# Generated by Django 5.1.2 on 2024-10-15 03:41

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_drill_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='comments',
            field=banjo.models.StringField(default=''),
        ),
    ]
