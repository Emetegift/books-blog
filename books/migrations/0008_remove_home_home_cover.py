# Generated by Django 4.2.3 on 2023-07-07 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='home_cover',
        ),
    ]