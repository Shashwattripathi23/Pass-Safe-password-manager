# Generated by Django 4.2.1 on 2023-06-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='logo',
            field=models.BinaryField(),
        ),
    ]
