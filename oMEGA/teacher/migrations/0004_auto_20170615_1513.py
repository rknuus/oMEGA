# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_exam_variables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variables', jsonfield.fields.JSONField(default={})),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='exam',
            name='content',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='variables',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Exam'),
        ),
    ]