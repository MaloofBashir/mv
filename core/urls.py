from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path("home",views.home,name='home'),
    path('erro',views.error,name='error'),
    path('index',views.index,name='index'),
    path('details',views.details,name='details'),
    path('addmovie',views.addmovie,name='addmovie'),
    path('showall',views.showall,name='showall'),
    path('showprivate',views.showprivate,name='showprivate'),
    path('logout',views.logout,name='logout')
]