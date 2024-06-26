# Generated by Django 4.2.9 on 2024-05-15 13:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0018_remove_video_cover_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='condition',
            field=models.CharField(choices=[('Used', 'Used'), ('New', 'New')], default='Used', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='overview_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='video_cover'),
        ),
    ]
