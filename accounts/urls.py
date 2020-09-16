from django.urls import path
from . import views

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
]

