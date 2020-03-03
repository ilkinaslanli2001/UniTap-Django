from django.urls import path
from .views import *
urlpatterns = [
    path('universitetler',mainpage,name="go_to_mainpage"),
    path('universitetler/<int:uniId>/',more_about_uni,name="go_to_more_uni"),
    path('',news,name="go_to_news"),
    path('news/',news,name="go_to_news"),
    path('news/<int:newsId>',more_about_news,name="go_to_more_news"),
    path('contactus/',contact_us,name="go_to_contact_us"),
    path('aboutus/',about_us,name="go_to_about_us"),
]

