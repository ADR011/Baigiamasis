# Generated by Django 4.0.3 on 2022-05-07 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0010_alter_metai_options_alter_metai_metai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metai',
            name='metai',
            field=models.DateField(blank=True, default=datetime.date(2022, 3, 1), max_length=20, null=True, verbose_name='automobilio pagaminimo metai'),
        ),
    ]