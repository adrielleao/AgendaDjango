from django.urls import path
from .views import HomeView, SignUpView, ContatoCreateView, ContatoListView, ContatoUpdateView, ContatoDeleteView, NomeListView

app_name = 'agenda'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cadastrar/', ContatoCreateView.as_view(), name='cadastrar'),
    path('listar/', ContatoListView.as_view(), name='listar'),
    path('editar/<int:pk>', ContatoUpdateView.as_view(), name='editar'),
    path('deletar/<int:pk>', ContatoDeleteView.as_view(), name='deletar'),
    path('buscar_nome/', NomeListView.as_view(),name='buscar_nome'),
    # path('buscar_letra', name='buscar_letra')
] 