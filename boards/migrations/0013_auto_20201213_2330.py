# Generated by Django 3.1.3 on 2020-12-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_boards_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]