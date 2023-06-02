from django.urls import path,include

from . import views

urlpatterns = [
   path('',views.IndexView.as_view(),name='index'),
   path('profile/',views.ProfileView.as_view(),name='profile'),
   path('',include('social_django.urls')),
   path('logout/',views.logout,name='logout')
]
