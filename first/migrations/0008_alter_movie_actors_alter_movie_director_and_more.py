# Generated by Django 4.0.5 on 2022-06-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_delete_sandwchich_delete_sauce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_title_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='production_company',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(max_length=500),
        ),
    ]