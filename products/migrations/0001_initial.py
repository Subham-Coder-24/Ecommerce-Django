# Generated by Django 4.2.4 on 2023-09-05 21:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models
import products.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(default='5', max_length=1)),
                ('content', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_order', models.CharField(max_length=255)),
                ('last_name_order', models.CharField(max_length=255)),
                ('delivery_method_order', models.IntegerField(choices=[(1, 'Courier delivery'), (2, 'Pickup at a parcel locker'), (3, 'Personal pickup')], default=1)),
                ('payment_method_order', models.IntegerField(choices=[(1, 'Cash/card payment on delivery'), (2, 'Online payment by credit card'), (3, 'Traditional money transfer')], default=1)),
                ('country_order', models.CharField(max_length=255)),
                ('city_order', models.CharField(max_length=255)),
                ('street_order', models.CharField(max_length=255)),
                ('house_number_order', models.CharField(max_length=255)),
                ('zip_code_order', models.CharField(max_length=255)),
                ('phone_number_order', models.CharField(max_length=255)),
                ('email_order', models.EmailField(max_length=255)),
                ('date_time_order', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default=products.models.get_default_image, storage=products.storage.OverriteFile(), upload_to=products.models.get_image_filepath)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('price', models.FloatField(max_length=64)),
                ('is_recommended', models.BooleanField(default=True)),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1.0)),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderproduct_order_id', to='products.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderproduct_product', to='products.product')),
            ],
        ),
    ]
