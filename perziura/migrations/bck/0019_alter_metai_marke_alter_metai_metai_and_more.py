# Generated by Django 4.0.3 on 2022-05-08 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0018_alter_klientas_modelis_spalva_metai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metai',
            name='marke',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perziura.modelis'),
        ),
        migrations.AlterField(
            model_name='metai',
            name='metai',
            field=models.CharField(blank=True, default='pass', max_length=20, null=True, verbose_name='metai'),
        ),
        migrations.AlterField(
            model_name='spalva',
            name='marke',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perziura.modelis'),
        ),
        migrations.AlterField(
            model_name='spalva',
            name='spalva',
            field=models.CharField(blank=True, default='pass', max_length=20, null=True, verbose_name='spalva'),
        ),
    ]