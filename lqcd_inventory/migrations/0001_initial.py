# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dilution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=5)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Eigensystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
                ('hyp_strength1', models.FloatField()),
                ('hyp_strength2', models.FloatField()),
                ('hyp_iterations', models.IntegerField()),
                ('eigenvector_count', models.IntegerField()),
                ('ev_ts_lambda_c', models.FloatField()),
                ('ev_ts_lambda_l', models.FloatField()),
                ('config_start', models.IntegerField()),
                ('config_end', models.IntegerField()),
                ('config_step', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ensemble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Perambulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass', models.FloatField()),
                ('quark_type', models.CharField(max_length=5)),
                ('config_start', models.IntegerField()),
                ('config_end', models.IntegerField()),
                ('config_step', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=2000, null=True)),
                ('dilution_sink_dirac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_sink_dirac', to='lqcd_inventory.Dilution')),
                ('dilution_sink_laph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_sink_laph', to='lqcd_inventory.Dilution')),
                ('dilution_sink_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_sink_space', to='lqcd_inventory.Dilution')),
                ('dilution_sink_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_sink_time', to='lqcd_inventory.Dilution')),
                ('dilution_source_dirac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_source_dirac', to='lqcd_inventory.Dilution')),
                ('dilution_source_laph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_source_laph', to='lqcd_inventory.Dilution')),
                ('dilution_source_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_source_space', to='lqcd_inventory.Dilution')),
                ('dilution_source_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_source_time', to='lqcd_inventory.Dilution')),
                ('eigensystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulators', to='lqcd_inventory.Eigensystem')),
            ],
        ),
        migrations.CreateModel(
            name='PerambulatorSeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_id', models.IntegerField()),
                ('seed', models.IntegerField()),
                ('perambulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator_seed', to='lqcd_inventory.Perambulator')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('account', models.CharField(blank=True, max_length=1000, null=True)),
                ('path', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='perambulator',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perambulator', to='lqcd_inventory.Storage'),
        ),
        migrations.AddField(
            model_name='eigensystem',
            name='ensemble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eigensystems', to='lqcd_inventory.Ensemble'),
        ),
        migrations.AddField(
            model_name='eigensystem',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eigensystem', to='lqcd_inventory.Storage'),
        ),
    ]