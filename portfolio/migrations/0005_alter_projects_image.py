# Generated by Django 3.2.9 on 2022-01-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_summary_summary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]