# Generated by Django 4.0.5 on 2022-07-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_remove_product_articles_product_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text11',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text12',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text13',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text14',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text15',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='articles', to='tracker.article'),
        ),
    ]