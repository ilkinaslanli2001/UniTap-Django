# Generated by Django 2.2.4 on 2019-08-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20190823_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uni_list',
            name='Dormitory',
            field=models.CharField(choices=[('Var', 'Var'), ('Yox du', 'Yox du')], max_length=100),
        ),
    ]