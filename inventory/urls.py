from django.urls import path

from inventory.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
