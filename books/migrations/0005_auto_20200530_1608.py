# Generated by Django 3.0.6 on 2020-05-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200530_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(),
        ),
    ]
