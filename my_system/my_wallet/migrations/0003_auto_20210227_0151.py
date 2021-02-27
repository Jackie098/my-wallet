# Generated by Django 3.1.6 on 2021-02-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0002_auto_20210227_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='operation',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='operation',
            name='trading_value',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='operation',
            name='unit_share_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]