from django.contrib import admin
from django.urls import path
from  home import views
urlpatterns = [
     path("",views.index,name= 'home'),
     path("about",views.about,name= 'about'), 
     path("services",views.services,name= 'services'),
     path("contact",views.contact,name= 'contact'),
     path("prelogin",views.prelogin,name= 'prelogin'),
     path("login1",views.adminlogin,name= 'login1'),
     path("login2/",views.login2,name= 'login2'),
     path("login3/",views.login3,name= 'login3'),
     path("login4/",views.login4,name= 'login4'),
     path("admin1" , views.admin1 , name='admin1'),
     path("admin2" , views.admin2 , name='admin2'),
     path("admin3" , views.admin3 , name='admin3'),
     path("admin4" , views.admin4 , name='admin4'),
    
     path("postadmin1/" , views.postadmin1 , name='postadmin1'),
     path("postadmin2/" , views.postadmin2 , name='postadmin2'),
     path("postadmin3/" , views.postadmin3 , name='postadmin3'),
     path("postadmin4/" , views.postadmin4 , name='postadmin4'),
     path("login/" , views.login ,name='login' ),
     path("lh1" , views.lh1 ,name='lh1' )
]