# Generated by Django 3.2.6 on 2021-08-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func_modeling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
