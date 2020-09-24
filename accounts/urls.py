from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# SET THE NAMESPACE!
app_name = 'accounts'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('', views.index,name='index'),
    path('home/', views.home, name='home'),
    path('special/', views.special, name='special'),
    path('register/',views.register,name='register'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tymtable/',views.tymtable,name='tymtable'),
    path('about/',views.about,name='about'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout'),
    path('c_tymtable/',views.c_tymtable,name='c_tymtable'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
