# Generated by Django 3.0.8 on 2020-08-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_merge_20200828_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
