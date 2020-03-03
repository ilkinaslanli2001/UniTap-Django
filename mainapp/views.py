from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.db.models import Q


def mainpage(request):
    uni_lists = uni_list.objects.all()
    query = request.GET.get('q')
    if query:
        uni_lists = uni_lists.filter(
            Q(UniName__icontains = query) 
           
        ).distinct()

    
    icon = icon_of_site.objects.all()[0]

    return render(request,"mainapp/uni_list.html",context = {
    "icon":icon,
    "uni_list":uni_lists,
    })


def more_about_uni(request,uniId):
    
    uni_data = uni_list.objects.filter(id=uniId)
    icon = icon_of_site.objects.all()[0]
    Images = []
    for i in uni_data:
        Images.append([i.UniImage1,i.UniImage2,i.UniImage3,i.UniImage4,i.UniImage5
                      ,i.UniImage6,i.UniImage7,i.UniImage8,i.UniImage9,i.UniImage10,
                      i.UniImage11,i.UniImage12,i.UniImage13,i.UniImage14,i.UniImage15])
    return render(request,"mainapp/more_about_uni.html",context=
        {
            "uni_data":uni_data,
            "Images":Images,
            "icon":icon,
        })



def view_404(request, *args, **kwargs):
    return render(request,'mainapp/404.html')


def contact_us(request):
    icon = icon_of_site.objects.all()[0]
    message=""
    name_and_surname= ""
    mail = ""
    if request.method =="POST":
        name_and_surname =  request.POST['name_and_surname']
        message = request.POST['message']
        mail = request.POST['mail']
        if(name_and_surname!="" and message!="" and mail!=""):
            info = "Name and Surname:"+name_and_surname+" mail:"+mail
            send_mail(info, message, settings.EMAIL_HOST_USER, ['endhigh002@gmail.com'])
            return render(request,"mainapp/contact.html",context=
                {
                        "icon":icon,
      
                })
       

    return render(request,"mainapp/contact.html",context=
                {
                        "icon":icon,
      
                })

def news(request):
    
     icon = icon_of_site.objects.all()[0]
     news  = news_model.objects.all().order_by('-id')
     if(news.count()>=21):
          news.last().delete()



       
     return render(request,"mainapp/news.html",context=
    {
        "icon":icon,
        "news":news,
    })
    
def more_about_news(request,newsId):
    
    news = news_model.objects.filter(id=newsId)
    other_news = news_model.objects.all()[:6]
    icon = icon_of_site.objects.all()[0]
    return render(request,"mainapp/more_about_news.html",context={
        "icon":icon,
        "news":news,
        "other_news":other_news,
        "current_news_id":newsId})


def about_us(request):
    icon = icon_of_site.objects.all()[0]
    return render(request,"mainapp/about_us.html",context={
        "icon":icon,
           })

