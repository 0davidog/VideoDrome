# Generated by Django 4.2.9 on 2024-04-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_video_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='certificate',
            field=models.CharField(choices=[('Not Rated', 'Not Rated'), ('U', 'U'), ('PG', 'PG'), ('12', '12'), ('15', '15'), ('18', '18')], default='Not Rated', max_length=250),
        ),
    ]
