# Generated by Django 4.2.9 on 2024-04-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='regioncode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
