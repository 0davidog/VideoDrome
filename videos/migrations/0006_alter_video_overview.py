# Generated by Django 4.2.9 on 2024-04-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='overview',
            field=models.TextField(blank=True),
        ),
    ]