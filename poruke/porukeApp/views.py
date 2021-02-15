from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm



from .models import *
from .forms import TelefoniForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('porukeApp:articles')


@login_required
def articles(req):
    tmp = Telefoni.objects.all()
    return render(req, 'articles.html', {'articles': tmp})


@login_required
def article(req, id):
    tmp = get_object_or_404(Telefoni, id=id)
    return render(req, 'article.html', {'article': tmp, 'page_title': tmp.markaTelefona})


@permission_required('poruke.change_article')
def edit(req, id):
    if req.method == 'POST':
        form = TelefoniForm(req.POST)

        if form.is_valid():
            a = Telefoni.objects.get(id=id)
            a.markaTelefona = form.cleaned_data['markaTelefona']
            a.modelTelefona = form.cleaned_data['modelTelefona']
            a.save()
            return redirect('porukeApp:articles')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Telefoni.objects.get(id=id)
        form = TelefoniForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('porukeApp.add_article')
def new(req):
    if req.method == 'POST':
        form = TelefoniForm(req.POST)

        if form.is_valid():
            a = Telefoni(markaTelefona=form.cleaned_data['markaTelefona'], modelTelefona=form.cleaned_data['modelTelefona'])
            a.save()
            return redirect('porukeApp:articles')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = TelefoniForm()
        return render(req, 'new.html', {'form': form})


def delete(req, id):
    if req.user.is_authenticated:
        if req.user.is_superuser:
             a= get_object_or_404(Telefoni , id = id)
             a.delete()
             return redirect('porukeApp:articles')

