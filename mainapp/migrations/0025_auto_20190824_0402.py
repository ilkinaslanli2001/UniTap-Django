# Generated by Django 2.2.4 on 2019-08-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20190823_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_model',
            name='Text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='Title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
