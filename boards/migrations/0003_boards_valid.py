# Generated by Django 3.1.3 on 2020-11-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20201121_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]
