# Generated by Django 3.0.8 on 2020-08-26 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_auto_20200825_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='BookTag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='novel',
            old_name='Noveltags',
            new_name='tags',
        ),
    ]
