from django.urls import path
from blog import views

urlpatterns = [
    path('wellcome/', views.ActivityTwo.wellCome),
    path('eco/<str:msg>/', views.ActivityTwo.eco),
    path('info/', views.ActivityTwo.api_info)
]

# urlpatterns = [
#     path('wellcome/', views..wellCome),
#     path('eco/<str:msg>/', views..eco),
#     path('info/', views..api_info)
# ]