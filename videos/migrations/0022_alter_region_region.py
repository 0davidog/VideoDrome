# Generated by Django 4.2.9 on 2024-05-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0021_alter_genre_genre_name_alter_language_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
