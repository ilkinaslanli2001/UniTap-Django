from django.db import models
from tinymce.widgets import TinyMCE
from phone_field import PhoneField
import datetime as dt
now = dt.datetime.now()
class icon_of_site(models.Model):

    cover = models.ImageField(upload_to='images/UniLogo',null=False,blank=False,verbose_name="Universitetin loqo tipi")

# Create your models here.




   
class uni_list(models.Model):

    UniName = models.CharField(max_length=250,null=False,blank=False,verbose_name="University name:")

    UniStudentsCount =  models.FloatField(null=True,blank=True,verbose_name="Student count:")
    UniYear = models.IntegerField(null=False,blank=False,default=now.year,verbose_name="Year:")
    UniMinPayment =  models.IntegerField(null=False,blank=False,default=1000,verbose_name="Min University fee:")
    UniMaxPayment= models.IntegerField(null=False,blank=False,default=1500,verbose_name="Min University fee:")
    YesNoCh=(
        ("Yes","Yes"),
        ("No","No"),
        )
    Dormitory = models.CharField(max_length=100,choices=YesNoCh,verbose_name="Dormitory:",default="No")
    
    UniWorkTime = models.TextField(null=True,blank=True,verbose_name="University work hours")
    UniGmail = models.CharField(max_length=250,null=False,blank=False,default = "None",verbose_name="Gmail:")
    UniNumber =PhoneField(blank=True, help_text='Contact phone number',verbose_name="Contact number:")
    UniWebsite =  models.URLField(null=True,blank=True,verbose_name="Website:")
    UniAdressForLink =  models.CharField(max_length=250,null=False,blank=False,verbose_name = "Google map link:")
    UniAdressForUser =  models.CharField(max_length=250,null=False,blank=False,verbose_name = "Adress:")
  
    UniImage1 = models.ImageField(null=False,blank=False,upload_to='images/UniLogos/',verbose_name="Photo:")
    UniImage2 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage3 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage4 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage5 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage6 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage7 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage8 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage9 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage10 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage11 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage12 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage13 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage14 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")
    UniImage15 = models.ImageField(null=True,blank=True,upload_to='images/UniPhotos/',verbose_name="Photo:")

    
class news_model(models.Model):
    Title = models.CharField(max_length=300,null=True,blank=False,verbose_name="Title:")
    Image =models.ImageField(blank = False,null = False,upload_to='images/NewsPhotos/',verbose_name="Photo:")
    
    Text = models.TextField(null=True,blank=True,verbose_name="Description:")
    Date = models.DateField(verbose_name="Date:")


   