# Generated by Django 4.1.1 on 2022-10-18 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familia', '0003_alter_familiar_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='nacimiento',
            field=models.CharField(max_length=10),
        ),
    ]