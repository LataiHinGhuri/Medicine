# Generated by Django 2.0.7 on 2018-08-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]