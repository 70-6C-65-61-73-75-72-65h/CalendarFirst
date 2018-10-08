from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Entry
from django.http import HttpResponse

# Create your views here.
def details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'myapp/details.html', {'entry':entry})

def index(request):
    # return HttpResponse("It works!")
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', {'entries': entries})
