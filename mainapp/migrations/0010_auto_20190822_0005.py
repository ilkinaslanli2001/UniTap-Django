# Generated by Django 2.2.4 on 2019-08-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20190821_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uni_list',
            name='UniAdressForLink',
            field=models.CharField(max_length=250, verbose_name='This link will redirect to the google Maps'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniAdressForUser',
            field=models.CharField(max_length=250, verbose_name='This is the readible link  for User'),
        ),
    ]
