# Generated by Django 4.1.4 on 2022-12-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=120),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]