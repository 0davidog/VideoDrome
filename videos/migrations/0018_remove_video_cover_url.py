# Generated by Django 4.2.9 on 2024-05-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0017_alter_video_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='cover_url',
        ),
    ]
