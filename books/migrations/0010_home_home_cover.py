# Generated by Django 4.2.3 on 2023-07-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_home_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='home_cover',
            field=models.CharField(default='page', max_length=1000),
        ),
    ]
