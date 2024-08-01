from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import About, Work, Gallery, Contact, Comment
from .forms import CommentForm

def home(request):
    about = About.objects.first()
    works = Work.objects.all()
    gallery = Gallery.objects.all()
    contact = Contact.objects.first()
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()

    context = {
        'about': about,
        'works': works,
        'gallery': gallery,
        'contact': contact,
        'comments': comments,
        'form': form
    }
    return render(request, 'home.html', context)

