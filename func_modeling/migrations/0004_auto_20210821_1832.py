# Generated by Django 3.2.6 on 2021-08-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func_modeling', '0003_alter_function_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='function',
            name='graph',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
