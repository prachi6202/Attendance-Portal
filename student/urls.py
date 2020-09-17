"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from accounts import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('accounts.urls',namespace='accounts')),
    path('home/', views.home, name='home'),
    path('tymtable/', views.tymtable, name='tymtable'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),
    path('index/',views.index,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='accounts/login.html')),

]
