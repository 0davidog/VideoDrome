# Generated by Django 4.2.9 on 2024-06-04 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_customermessagethread_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermessagethread',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomerMessage',
        ),
        migrations.DeleteModel(
            name='CustomerMessageThread',
        ),
    ]
