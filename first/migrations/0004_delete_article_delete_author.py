# Generated by Django 4.0.5 on 2022-06-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_author_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
