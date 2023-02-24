from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_data,name='home'),
    path('edit/<int:id>', views.edit,name='edit'),
    
    # path('delete/<int:id>', views.delete,name='delete'),  
    path('<int:id>', views.delete,name='delete'),  

]
