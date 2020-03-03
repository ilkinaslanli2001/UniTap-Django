# Generated by Django 2.2.4 on 2019-08-22 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_uni_list_uniyear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uni_list',
            old_name='UniUrl',
            new_name='UniWebsite',
        ),
        migrations.AddField(
            model_name='uni_list',
            name='UniMaxCountOfMoney',
            field=models.IntegerField(default=1500),
        ),
        migrations.AddField(
            model_name='uni_list',
            name='UniMinCountOfMoney',
            field=models.IntegerField(default=1000),
        ),
    ]