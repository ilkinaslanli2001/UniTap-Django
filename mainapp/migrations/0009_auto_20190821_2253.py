# Generated by Django 2.2.4 on 2019-08-21 19:53

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20190821_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uni_list',
            name='UniNumber',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]