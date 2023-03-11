from django.urls import path

from inventory.views import HomeView, GameFormView, GameListView, GameDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add', GameFormView.as_view(), name='add_game'),
    path('games', GameListView.as_view(), name='games'),
    path('game/<int:pk>', GameDetailView.as_view(), name='game'),
]
