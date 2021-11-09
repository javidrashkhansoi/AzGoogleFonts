from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('designer/<slug:designer_slug>', views.home, name='designer'),
    path('group/<slug:group_slug>', views.home, name='group'),
]
