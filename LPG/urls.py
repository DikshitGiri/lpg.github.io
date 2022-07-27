"""LPG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('base/',views.base, name="base"),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('login/',views.customerlogin, name="login"),
    path('logout/',views.customerlogout, name="logout"),
    
    path('gasordered/',views.gasordered, name="gasordered"),
    path('register/',views.register, name="register"),
   
    path('customerdashboard/',views.customerdashboard, name="customerdashboard"),
    path('bookgas/',views.bookgas, name="bookgas"),
    path('bookedgas/',views.bookedgas, name="bookedgas"),
    path('profileinfo/',views.profileinfo, name="profileinfo"),
    path('',views.landingheader, name="landingheader"),

    

 
    path ('sindex/', views.sindex, name="sndex"),
    path ('viewdata/', views.viewdata, name="viewdata"),
   

    path ('gasentry/', views.entry, name="gasentry"),
    path ('search', views.search, name="search"),
    
    path ('body/', views.body, name="body"),
    path('supplierin/',views.supplierin,name="supplier"),
    path('supplierlogin/',views.supplierlogin,name="supplierlogin"),
    
    path('supplierdashboard/',views.supplierdashboard, name="supplierdashboard"),
    path('supplierout/',views.supplierout,name="supplierout"),
    path('gasentry/',views.entry,name="gasentry"),
    path('gasupdate/<str:pk>',views.gas_update,name="gasupdate"),
    path('gasdelete/<str:pk>',views.gas_delete,name="gasdelete"),
    path('status/',views.status,name="status"),
    path('report/',views.report,name="report"),
    path('category/',views.category,name="category"),
  
    # path('delete_gas/<gas_id>',views.gas_delete,name='gas_delete')

    
    
    
    # path('',include('Accounts.urls'))
]
