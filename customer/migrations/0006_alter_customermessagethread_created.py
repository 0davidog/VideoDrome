# Generated by Django 4.2.9 on 2024-05-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customermessagethread_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermessagethread',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]