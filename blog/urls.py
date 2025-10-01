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
]

# urlpatterns = [
#     path('wellcome/', views..wellCome),
#     path('eco/<str:msg>/', views..eco),
#     path('info/', views..api_info)
# ]