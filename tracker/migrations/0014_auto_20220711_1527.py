# Generated by Django 3.2.11 on 2022-07-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_auto_20220711_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='perFat',
            new_name='percentFat',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='perventProtein',
            new_name='percenttProtein',
        ),
    ]
