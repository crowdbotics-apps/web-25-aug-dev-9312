# Generated by Django 2.2.15 on 2020-08-25 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200825_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='key1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='key2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='key3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='key4',
        ),
    ]
