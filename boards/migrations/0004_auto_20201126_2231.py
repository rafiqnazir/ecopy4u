# Generated by Django 3.1.3 on 2020-11-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_boards_valid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boards',
            unique_together={('board_name', 'class_number', 'subject', 'year', 'sereis')},
        ),
    ]