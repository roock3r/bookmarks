# Generated by Django 3.2.12 on 2022-03-29 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=512),
        ),
    ]