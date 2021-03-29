from django.urls import path
from games import views

app_name = 'games'

urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
]
