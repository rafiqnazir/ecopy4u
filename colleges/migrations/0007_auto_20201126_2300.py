# Generated by Django 3.1.3 on 2020-11-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0006_auto_20201126_2259'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='colleges',
            unique_together={('college_name', 'branch', 'subject')},
        ),
    ]
