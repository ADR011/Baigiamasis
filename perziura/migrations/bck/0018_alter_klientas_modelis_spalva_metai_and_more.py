# Generated by Django 4.0.3 on 2022-05-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perziura', '0017_alter_klientas_modelis_alter_modelis_modelis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klientas',
            name='modelis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perziura.modelis'),
        ),
        migrations.CreateModel(
            name='Spalva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spalva', models.CharField(blank=True, default='pass', max_length=20, null=True)),
                ('marke', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perziura.marke')),
            ],
        ),
        migrations.CreateModel(
            name='Metai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metai', models.CharField(blank=True, default='pass', max_length=20, null=True)),
                ('marke', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perziura.marke')),
            ],
        ),
        migrations.AlterField(
            model_name='klientas',
            name='metai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perziura.metai'),
        ),
        migrations.AlterField(
            model_name='klientas',
            name='spalva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perziura.spalva'),
        ),
    ]