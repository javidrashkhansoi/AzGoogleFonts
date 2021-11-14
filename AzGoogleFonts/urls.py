from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('designer/<slug:designer_slug>', views.home, name='designer'),
    path('group/<slug:group_slug>', views.home, name='group'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('googleb99dd86e1faa8821.html/', views.google, name='google'),
    path('font/<slug:font_slug>', views.font, name='font'),
]
