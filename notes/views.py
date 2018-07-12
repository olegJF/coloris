from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *

def home(request):
    form = NoteModelForm
    if request.method == "POST":
        form = NoteModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка добавлена!')
            
        return redirect('/')
    
    else:
        qs = Note.objects.all()
        
        return render(request, 'notes/home.html', {'form': form, 'list': qs})
