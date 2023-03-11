from django.urls import path

from inventory.views import HomeView, GameFormView, GameListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add', GameFormView.as_view(), name='add_game'),
    path('games', GameListView.as_view(), name='games'),
]
