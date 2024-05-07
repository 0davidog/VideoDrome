# Generated by Django 4.2.9 on 2024-05-07 10:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('f9310608-076c-40e5-a688-c71f330c2074'), editable=False),
        ),
        migrations.DeleteModel(
            name='OrderBasket',
        ),
    ]