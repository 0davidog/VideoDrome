# Generated by Django 4.2.9 on 2024-04-22 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250)),
                ('certificate', models.CharField(choices=[('1', 'Not Rated'), ('2', 'U'), ('3', 'PG'), ('4', '12'), ('5', '15'), ('6', '18')], default='1', max_length=250)),
                ('format', models.CharField(choices=[('1', 'DVD'), ('2', 'Blu-Ray'), ('3', '4K Ultra HD'), ('4', 'Dual Format: Blu-Ray and DVD'), ('5', 'Dual Format: UHD and Blu-Ray')], default='1', max_length=250)),
                ('discs', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='')),
                ('cover_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('overview', models.TextField(blank=True, max_length=500)),
                ('release_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('on_sale', models.BooleanField(default=False)),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('languages', models.ManyToManyField(blank=True, to='videos.language')),
                ('region', models.ManyToManyField(blank=True, to='videos.region')),
                ('subtitles', models.ManyToManyField(blank=True, to='videos.subtitle')),
                ('wishlist', models.ManyToManyField(blank=True, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]