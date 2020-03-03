from django.contrib import admin
from .models import *
class news_model_Admin(admin.ModelAdmin):
    list_display = ["Title"]
    fieldsets=[
        ('Title and Image',{"fields":["Title","Image"]}),
        ('Text',{"fields":["Text"]}),
        ('Date',{"fields":["Date"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
      
        }
class uni_list_Admin(admin.ModelAdmin):
    search_fields = ['UniName','UniData']
    list_filter = ['UniName']
    list_display = ['UniName']
    fieldsets=[
        ('Universitetin adı',{"fields":["UniName"]}),
        ('Şagirdlərin sayı',{"fields":["UniStudentsCount"]}),
        ('Həmin ilin maksimum və minimum ödənişi',{"fields":["UniYear", "UniMinPayment",  "UniMaxPayment"]}),
        ('Yataqxana',{"fields":["Dormitory"]}),
        ('Əlaqə nömrəsi,Gmail və Universitetin iş vaxtları',{"fields":["UniNumber","UniGmail","UniWorkTime"]}),
        ('Universitetin veb səhifəsi',{"fields":["UniWebsite"]}),
        ('Universitetin şəkilləri',{"fields":["UniImage1","UniImage2","UniImage3","UniImage4","UniImage5","UniImage6","UniImage7",
                                            "UniImage8","UniImage9","UniImage10","UniImage11","UniImage12","UniImage13","UniImage14","UniImage15"]}),
        ("Universitetin adresi",{"fields":["UniAdressForLink", "UniAdressForUser"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
       
        }
admin.site.register(icon_of_site)
admin.site.register(uni_list,uni_list_Admin)
admin.site.register(news_model,news_model_Admin)

