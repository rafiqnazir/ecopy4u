# Generated by Django 3.1.3 on 2020-11-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20201126_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='board_name',
            field=models.CharField(default='JKBOSE', max_length=50),
        ),
        migrations.AlterField(
            model_name='boards',
            name='class_number',
            field=models.IntegerField(),
        ),
    ]
