# Generated by Django 3.1.3 on 2020-11-27 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0007_auto_20201127_2233'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='boards',
            name='unique board',
        ),
    ]
