# Generated by Django 5.0 on 2024-03-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_stock', '0002_remove_stockprice_adj_close_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]