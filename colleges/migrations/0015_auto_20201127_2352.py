# Generated by Django 3.1.3 on 2020-11-27 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0014_auto_20201127_2346'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='colleges',
            unique_together={('college_name', 'branch', 'subject', 'year', 'exam')},
        ),
    ]
