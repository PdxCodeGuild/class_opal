# Generated by Django 4.1.4 on 2022-12-28 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_alter_item_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
    ]
