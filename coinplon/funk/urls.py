from django.urls import path, include
from . import views

urlpatterns = [

    path('func_list/', views.FunctionalityListView.as_view(), name='func_list'),

    path('func_detail/<int:pk>',views.FunctionalityDetailView.as_view(), name="func_detail")
         #une primary key qui va nous permettre de retrouver l'instance qui ns interesse (l'id)
   
  
]