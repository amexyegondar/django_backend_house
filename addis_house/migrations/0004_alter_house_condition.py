# Generated by Django 4.2.11 on 2024-04-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addis_house', '0003_house_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='condition',
            field=models.TextField(),
        ),
    ]
