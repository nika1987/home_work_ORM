# Generated by Django 4.2.4 on 2023-10-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_is_published_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
    ]