# Generated by Django 4.2.9 on 2024-04-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_video_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='director',
            field=models.CharField(max_length=250, null=True),
        ),
    ]