# Generated by Django 3.1.3 on 2020-11-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0011_auto_20201126_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='branch',
            field=models.CharField(choices=[('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics Engineering', 'Electronics Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering'), ('Information & Technology', 'Information & Technology')], max_length=50),
        ),
    ]
