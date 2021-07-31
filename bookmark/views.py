from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark