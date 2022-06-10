# Generated by Django 4.0.5 on 2022-06-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_author_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sandwchich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sauce', models.ManyToManyField(to='first.sauce')),
            ],
        ),
    ]