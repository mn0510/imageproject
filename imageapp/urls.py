from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.index,name='index'),
   path('add',views.add,name='add'),
   path('details',views.details,name='details'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),

    path('back',views.back,name='back')

]