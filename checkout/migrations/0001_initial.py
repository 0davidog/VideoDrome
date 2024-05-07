# Generated by Django 4.2.9 on 2024-05-05 13:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0016_alter_video_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.UUIDField(default=uuid.UUID('5e25ff4f-eccb-491a-a56e-b09d70ef2785'), editable=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('basket_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_quantity', models.IntegerField(default=0)),
                ('basket_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('basket_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_basket', to='checkout.order')),
            ],
        ),
    ]