# Generated by Django 5.0.3 on 2024-04-15 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorystay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('bringer', models.CharField(blank=True, max_length=200, null=True)),
                ('timein', models.DateTimeField(blank=True, default=0, null=True)),
                ('timeout', models.DateTimeField(blank=True, default=0, null=True)),
                ('c_stay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoapp.categorystay')),
            ],
        ),
    ]
