#Mapear caminhos para as funções
from django.urls import path
from . import views

#Configuração de URL
app_name = 'playground'
urlpatterns = [
    #Retorna a Url Patern de um objeto
    path('hello/', views.say_hello),

    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]