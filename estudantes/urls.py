from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('<int:id>', views.ver_estudante, name='ver_estudante'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
]