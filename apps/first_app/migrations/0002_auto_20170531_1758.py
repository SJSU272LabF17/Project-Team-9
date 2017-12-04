# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=38)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='eml',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='f_n',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='l_n',
        ),
        migrations.AddField(
            model_name='user',
            name='h_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_items', to='first_app.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='wished_users',
            field=models.ManyToManyField(related_name='wished_items', to='first_app.User'),
        ),
    ]
