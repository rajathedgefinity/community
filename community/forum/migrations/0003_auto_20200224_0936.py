# Generated by Django 2.2.8 on 2020-02-24 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_allthreads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allthreads',
            old_name='user_id',
            new_name='user',
        ),
    ]