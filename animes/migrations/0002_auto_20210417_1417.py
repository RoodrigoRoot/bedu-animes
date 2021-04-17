# Generated by Django 3.2 on 2021-04-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='broadcast_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='end_airing',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genres',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='licensors',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='producers',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='start_airing',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='starting_season',
            field=models.CharField(max_length=100),
        ),
    ]
