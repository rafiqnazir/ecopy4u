# Generated by Django 3.1.3 on 2020-11-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colleges',
            old_name='year',
            new_name='session',
        ),
        migrations.AlterUniqueTogether(
            name='colleges',
            unique_together={('college_name', 'branch', 'session')},
        ),
    ]
