# Generated by Django 4.1.5 on 2023-01-27 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalized_index', '0006_alter_stock_country_alter_stock_dividend_yield_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalizedIndexStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_weight', models.FloatField(null=True)),
                ('target_allocation', models.FloatField(null=True)),
                ('current_price', models.FloatField(null=True)),
                ('quantity', models.FloatField(null=True)),
                ('order_quantity', models.FloatField(null=True)),
                ('rounding_loss', models.FloatField(null=True)),
                ('personalized_index_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalized_indexes', to='personalized_index.personalizedindex')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='personalized_index.stock')),
            ],
        ),
    ]