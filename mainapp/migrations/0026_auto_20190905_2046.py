# Generated by Django 2.2.4 on 2019-09-05 17:46

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_auto_20190824_0402'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhotoTag',
        ),
        migrations.AlterField(
            model_name='icon_of_site',
            name='cover',
            field=models.ImageField(upload_to='images/UniLogo', verbose_name='Universitetin loqo tipi'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='Date',
            field=models.DateField(verbose_name='Tarix:'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='Image',
            field=models.ImageField(upload_to='images/NewsPhotos/', verbose_name='Xəbərin şəkili:'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='Text',
            field=models.TextField(blank=True, null=True, verbose_name='Xəbər haqda məlumat:'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='Title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Xəbərin adı:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='Dormitory',
            field=models.CharField(choices=[('Var', 'Yox'), ('Yox du', 'Yox du')], max_length=100, verbose_name='Yataqxana:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniGmail',
            field=models.CharField(default='None', max_length=250, verbose_name='Gmail:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage1',
            field=models.ImageField(upload_to='images/UniLogos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage10',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage11',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage12',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage13',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage14',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage15',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage2',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage3',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage4',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage5',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage6',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage7',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage8',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniImage9',
            field=models.ImageField(blank=True, null=True, upload_to='images/UniPhotos/', verbose_name='Şəkil:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniMaxPayment',
            field=models.IntegerField(default=1500, verbose_name='Maksimum ödəniş:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniMinPayment',
            field=models.IntegerField(default=1000, verbose_name='Minimum ödəniş:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniName',
            field=models.CharField(max_length=250, verbose_name='Universitetin adı:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniNumber',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, verbose_name='Əlaqə nömrəsi'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniStudentsCount',
            field=models.FloatField(blank=True, null=True, verbose_name='Şagirdlərin sayı:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniWebsite',
            field=models.URLField(blank=True, null=True, verbose_name='Universitetin veb səhifəsi:'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniWorkTime',
            field=models.TextField(blank=True, null=True, verbose_name='Universitetin iş vaxtları'),
        ),
        migrations.AlterField(
            model_name='uni_list',
            name='UniYear',
            field=models.IntegerField(default=2019, verbose_name='Nəzərdə tutulmuş il:'),
        ),
    ]
