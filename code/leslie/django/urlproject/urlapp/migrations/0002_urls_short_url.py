# Generated by Django 4.1.4 on 2022-12-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='short_url',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
