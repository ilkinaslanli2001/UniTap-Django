# Generated by Django 2.2.4 on 2019-09-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20190905_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_model',
            name='Title',
            field=models.CharField(max_length=300, null=True, verbose_name='Xəbərin adı:'),
        ),
    ]
