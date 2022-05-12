# Generated by Django 4.0.3 on 2022-05-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0006_remove_klientas_klientas_klientas_klientas_pavarde_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='gimimo_data',
        ),
        migrations.AddField(
            model_name='klientas',
            name='klientas_email',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='klientas',
            name='klientas_spalva',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Automobilio spalva'),
        ),
        migrations.AlterField(
            model_name='klientas',
            name='klientas_pavarde',
            field=models.CharField(max_length=124, null=True, verbose_name='kliento pavarde'),
        ),
        migrations.AlterField(
            model_name='klientas',
            name='klientas_vardas',
            field=models.CharField(max_length=124, null=True, verbose_name='kliento vardas'),
        ),
    ]