# Generated by Django 4.2.4 on 2023-10-10 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_blogpost_is_published_blogpost_views_count_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]