# Generated by Django 4.2.9 on 2024-04-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_region_regioncode_alter_region_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='aspect_ratio',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='video',
            name='format',
            field=models.CharField(choices=[('DVD', 'DVD'), ('Blu-Ray', 'Blu-Ray'), ('4K Ultra HD', '4K Ultra HD'), ('Dual Format: Blu-Ray and DVD', 'Dual Format: Blu-Ray and DVD'), ('Dual Format: UHD and Blu-Ray', 'Dual Format: UHD and Blu-Ray')], default='DVD', max_length=250),
        ),
    ]