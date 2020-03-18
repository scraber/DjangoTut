from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Game


def home(request):
    return render(request, "boardgames/base.html")


class GameListView(ListView):
    model = Game
    template_name = "boardgames/browse.html"
    context_object_name = "games"
    ordering = ["name"]


class GameDetailView(DetailView):
    model = Game


class GameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "boardgames.add_game"
    permission_denied_message = " Only Skarabeusz is allowed to add more games "
    model = Game
    fields = [
        "name",
        "max_players_count",
        "age_restriction",
        "difficulty",
        "rng_factor",
        "genre",
    ]


class GameUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "boardgames.change_game"
    permission_denied_message = " Only Skarabeusz is allowed to edit game info "
    model = Game
    fields = [
        "name",
        "max_players_count",
        "age_restriction",
        "difficulty",
        "rng_factor",
        "genre",
    ]


class GameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "boardgames.delete_game"
    permission_denied_message = " Only Skarabeusz is allowed to delete game "
    model = Game
    success_url = reverse_lazy("boardgames-home")
