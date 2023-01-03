# Generated by Django 4.1.4 on 2022-12-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_urls_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='short_url',
        ),
        migrations.AddField(
            model_name='urls',
            name='short_code',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='long_url',
            field=models.URLField(),
        ),
    ]
