# Generated by Django 3.0 on 2020-02-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
