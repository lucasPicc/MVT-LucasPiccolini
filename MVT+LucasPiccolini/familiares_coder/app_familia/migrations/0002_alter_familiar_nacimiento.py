# Generated by Django 4.1.1 on 2022-10-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='nacimiento',
            field=models.IntegerField(),
        ),
    ]