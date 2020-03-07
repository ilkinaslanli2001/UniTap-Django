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
        ('Universitetin name',{"fields":["UniName"]}),
        ('Student count',{"fields":["UniStudentsCount"]}),
        ('Max and Min University Fee of current year',{"fields":["UniYear", "UniMinPayment",  "UniMaxPayment"]}),
        ('Dormitory',{"fields":["Dormitory"]}),
        ('Contact Number, Gmail və University work hours',{"fields":["UniNumber","UniGmail","UniWorkTime"]}),
        ('Universitetiy website',{"fields":["UniWebsite"]}),
        ('Universitety photos',{"fields":["UniImage1","UniImage2","UniImage3","UniImage4","UniImage5","UniImage6","UniImage7",
                                            "UniImage8","UniImage9","UniImage10","UniImage11","UniImage12","UniImage13","UniImage14","UniImage15"]}),
        ("Universitety address",{"fields":["UniAdressForLink", "UniAdressForUser"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
       
        }
admin.site.register(icon_of_site)
admin.site.register(uni_list,uni_list_Admin)
admin.site.register(news_model,news_model_Admin)

