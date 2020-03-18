from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="boardgames-home"),
    path("browse/", views.GameListView.as_view(), name="games-browse"),
    path("game/<int:pk>/", views.GameDetailView.as_view(), name="game-detail"),
    path("game/new/", views.GameCreateView.as_view(), name="game-create"),
    path("game/<int:pk>/update/", views.GameUpdateView.as_view(), name="game-update"),
    path("game/<int:pk>/delete/", views.GameDeleteView.as_view(), name="game-delete"),
]
