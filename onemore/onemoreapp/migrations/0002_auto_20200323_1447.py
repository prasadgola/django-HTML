# Generated by Django 2.2.5 on 2020-03-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onemoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetoone',
            name='onetooneid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weeklypresentation',
            name='weeklypresentationid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
