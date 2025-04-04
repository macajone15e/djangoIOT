# Generated by Django 5.1.5 on 2025-04-02 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('lastSeenAt', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField()),
                ('room', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('attach', models.PositiveIntegerField(default=0)),
                ('otaPassword', models.CharField(max_length=100)),
                ('sensorDelay', models.PositiveIntegerField(default=0)),
                ('rssi', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='Temperatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temperatures', to='iot.devices')),
            ],
            options={
                'verbose_name': 'Temperature',
                'verbose_name_plural': 'Temperatures',
            },
        ),
    ]
