# Generated by Django 4.2.9 on 2024-05-07 14:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0016_alter_video_sku'),
        ('checkout', '0002_remove_order_basket_total_remove_order_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoOrderBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('eb94b665-f62f-4b00-bcc7-fb6950a1b687'), editable=False),
        ),
        migrations.CreateModel(
            name='VideoOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitiy', models.IntegerField(default=0)),
                ('video_sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_order', to='checkout.videoorderbasket')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_order_items', to='checkout.order')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
        ),
        migrations.AddField(
            model_name='videoorderbasket',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_total', to='checkout.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_order', to='checkout.customer'),
            preserve_default=False,
        ),
    ]
