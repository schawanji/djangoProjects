from django.urls import path,include
from . import views

urlpatterns = [
    
    path('state/list/', views.ListState.as_view(), name='statelist'),
    path('state/create', views.StateFormCreate.as_view(), name='createstate'),
    path('attraction/create', views.AttractionFormCreate.as_view(), name='createattraction'),
    
]
