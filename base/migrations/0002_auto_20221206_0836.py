# Generated by Django 3.2 on 2022-12-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout',
            field=models.DateField(),
        ),
    ]