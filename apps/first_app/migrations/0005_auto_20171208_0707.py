# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-08 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('status', models.CharField(max_length=38)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=38)),
                ('template', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='first_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.TextField()),
                ('content', models.TextField()),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklist_id', to='first_app.Checklist')),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='container_id', to='first_app.Container'),
        ),
    ]
