# Generated by Django 4.2.9 on 2024-05-12 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_customerorder_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('0ec5856b-63cb-4b46-81e1-ee871e351c7c'), editable=False),
        ),
    ]
