from django.urls import path
from . import views

#criando uma rota para aplicação
urlpatterns = [
    #ele pegara a função meu_app, que foi direcionada pelo arquivo url da pasta do projeto
    path('meu_app/', views.meu_app, name='meu_app'),
    path('meu_app/detalhe.html/', views.detalhe, name='detalhe.html'),
]