# Generated by Django 4.2.3 on 2023-07-04 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('coll_cover', models.CharField(max_length=1000)),
                ('coll_buy', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('piececover', models.CharField(max_length=1000)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.collection')),
            ],
        ),
    ]
