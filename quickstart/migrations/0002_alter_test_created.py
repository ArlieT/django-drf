# Generated by Django 4.2.7 on 2023-11-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
