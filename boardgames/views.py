from django.shortcuts import render


games = [
    {
        'players_count': 5,
        'name': 'Catan',
        'genre': 'Dice Rolling'
    },
    {
        'players_count': 7,
        'name': '7 Wonders',
        'genre': 'Deck building'
    },
    {
        'players_count': 6,
        'name': 'Talisman',
        'genre': 'Dice Rolling'
    },
]


def home(request):
    context = {
        'games': games
    }
    return render(request, 'boardgames/home.html', context)


def about(request):
    return render(request, 'boardgames/about.html', {'title': 'About'})
