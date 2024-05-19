# Generated by Django 4.2.9 on 2024-05-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0019_video_condition_video_overview_source_video_trailer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='video', to='videos.language'),
        ),
        migrations.AlterField(
            model_name='video',
            name='region',
            field=models.ManyToManyField(blank=True, related_name='video', to='videos.region'),
        ),
        migrations.AlterField(
            model_name='video',
            name='subtitles',
            field=models.ManyToManyField(blank=True, related_name='video', to='videos.subtitle'),
        ),
    ]
