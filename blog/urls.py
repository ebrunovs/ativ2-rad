from django.urls import path
from blog import views

urlpatterns = [
    path('wellcome/', views.ActivityTwo.wellCome),
    path('eco/<str:msg>/', views.ActivityTwo.eco),
    path('info/', views.ActivityTwo.api_info),
    path('home/', views.ActivityThree.home, name='home'),
    path('contato/<int:ctt>/', views.ActivityThree.contato, name='contato'),
    path('homet/', views.ActivityThree.homeTemplate, name='homet'),
    path('aboutt/', views.ActivityThree.aboutTemplate, name='about'),
    
    # Dashboard principal
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # URLs para Autor
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/novo/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/deletar/', views.AutorDeleteView.as_view(), name='autor_delete'),
    
    # URLs para Editora
    path('editoras/', views.EditoraListView.as_view(), name='editora_list'),
    path('editoras/novo/', views.EditoraCreateView.as_view(), name='editora_create'),
    path('editoras/<int:pk>/editar/', views.EditoraUpdateView.as_view(), name='editora_update'),
    path('editoras/<int:pk>/deletar/', views.EditoraDeleteView.as_view(), name='editora_delete'),
    
    # URLs para Livro
    path('livros/', views.LivroListView.as_view(), name='livro_list'),
    path('livros/novo/', views.LivroCreateView.as_view(), name='livro_create'),
    path('livros/<int:pk>/editar/', views.LivroUpdateView.as_view(), name='livro_update'),
    path('livros/<int:pk>/deletar/', views.LivroDeleteView.as_view(), name='livro_delete'),
    
    # URLs para Publica
    path('publicacoes/', views.PublicaListView.as_view(), name='publica_list'),
    path('publicacoes/novo/', views.PublicaCreateView.as_view(), name='publica_create'),
    path('publicacoes/<int:pk>/editar/', views.PublicaUpdateView.as_view(), name='publica_update'),
    path('publicacoes/<int:pk>/deletar/', views.PublicaDeleteView.as_view(), name='publica_delete'),

    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
]

# urlpatterns = [
#     path('wellcome/', views..wellCome),
#     path('eco/<str:msg>/', views..eco),
#     path('info/', views..api_info)
# ]