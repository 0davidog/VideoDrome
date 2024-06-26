# Generated by Django 4.2.9 on 2024-05-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0020_alter_genre_genre_name_alter_language_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='regioncode',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
