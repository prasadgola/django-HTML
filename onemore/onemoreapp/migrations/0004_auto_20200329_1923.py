# Generated by Django 2.2.5 on 2020-03-29 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onemoreapp', '0003_auto_20200326_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklypresentation',
            old_name='userid',
            new_name='user',
        ),
    ]
