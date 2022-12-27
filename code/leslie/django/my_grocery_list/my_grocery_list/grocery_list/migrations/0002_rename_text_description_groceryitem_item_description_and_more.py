# Generated by Django 4.1.4 on 2022-12-22 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groceryitem',
            old_name='text_description',
            new_name='item_description',
        ),
        migrations.RemoveField(
            model_name='groceryitem',
            name='is_complete',
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
