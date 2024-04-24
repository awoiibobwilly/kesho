# Generated by Django 5.0.3 on 2024-04-16 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keshoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payamount', models.IntegerField(blank=True, null=True)),
                ('paynum', models.IntegerField(blank=True, null=True)),
                ('paycurrency', models.CharField(blank=True, default='ugx', max_length=10, null=True)),
                ('c_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoapp.categorystay')),
            ],
        ),
        migrations.AddField(
            model_name='attendees',
            name='b_fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoapp.payment'),
        ),
    ]