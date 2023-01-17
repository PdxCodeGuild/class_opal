# Generated by Django 4.1.4 on 2022-12-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('cohort', models.CharField(max_length=200)),
                ('favorite_topic', models.CharField(max_length=200)),
                ('favorite_teacher', models.CharField(max_length=200)),
                ('capstone', models.URLField(max_length=250)),
            ],
        ),
    ]