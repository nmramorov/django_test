# Generated by Django 3.1.7 on 2021-05-18 17:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=50)),
                ('second_name', models.TextField(max_length=50)),
                ('additional_info', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=datetime.datetime(2021, 5, 18, 17, 46, 20, 12382, tzinfo=utc))),
                ('first_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First user+', to='api.user')),
                ('second_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Second user+', to='api.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='friendship',
            constraint=models.UniqueConstraint(fields=('first_user_id', 'second_user_id'), name='fst_constraint'),
        ),
    ]
