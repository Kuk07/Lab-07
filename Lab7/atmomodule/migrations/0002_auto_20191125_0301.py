# Generated by Django 2.2.7 on 2019-11-25 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atmomodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtmoSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('temperature', models.FloatField()),
                ('pressure', models.FloatField()),
                ('co2_level', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('create_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SensorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AtmoSensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atmomodule.SensorCategory'),
        ),
        migrations.AddField(
            model_name='atmosnapshot',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atmomodule.Sensor'),
        ),
    ]
