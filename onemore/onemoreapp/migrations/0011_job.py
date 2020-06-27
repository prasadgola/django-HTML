# Generated by Django 2.2.5 on 2020-06-23 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onemoreapp', '0010_jvtthankyou'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('jobid', models.AutoField(primary_key=True, serialize=False)),
                ('recname', models.CharField(max_length=100)),
                ('recexp', models.CharField(max_length=100)),
                ('recctc', models.CharField(max_length=100)),
                ('recdate', models.DateField(null=True)),
                ('reccomname', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onemoreapp.users')),
            ],
        ),
    ]
