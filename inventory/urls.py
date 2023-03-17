from django.urls import path, include
from rest_framework import routers

from inventory import views
from inventory.views import HomeView, GameFormView, GameListView, GameDetailView

router = routers.DefaultRouter()
router.register(r'game', views.GameViewSet, 'game')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomeView.as_view(), name='home'),
    path('add', GameFormView.as_view(), name='add_game'),
    path('games', GameListView.as_view(), name='games'),
    path('game/<int:pk>', GameDetailView.as_view(), name='game'),
]
