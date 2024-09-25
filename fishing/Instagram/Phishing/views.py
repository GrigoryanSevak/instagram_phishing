from django.shortcuts import render
from .models import Users
from .forms import UsersForm
import webbrowser


def index(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            news = form.save()
            # webbrowser.open('https://www.instagram.com/reel/C4iL6IMsvLu/?igsh=OWl5Y3R5dXMzOHQy', new=2)
    else:
        form =  UsersForm()
    return render(request, 'Instagram/index.html', {'form': form})
