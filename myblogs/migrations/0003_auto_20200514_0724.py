# Generated by Django 2.2.4 on 2020-05-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0002_auto_20200513_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
