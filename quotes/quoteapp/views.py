import json
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Quote, Author


# Create your views here.

def main(request):
    quotes = Quote.objects.all()[:10]
    all_tags = []
    return render(request, 'quoteapp/index.html', {"quotes": quotes, 'name': 'Hello name', 'all_tags': all_tags})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        return render(request, 'quoteapp/author.html', {'form': form})
    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


@login_required
def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)
                return redirect(to='quoteapp:main')
            else:
                return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': QuoteForm()})


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        return render(request, 'quoteapp/tag.html', {'form': form})
    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def info(request):
    auothors = Author.objects.all()
    return render(request, 'quoteapp/info.html', {"auothors": auothors})


def author_page(request, author_id):
    info_author = Author.objects.filter(pk=author_id)
    return render(request, 'quoteapp/detail_author.html', context={"info_author": info_author})


def seed_db():
    author_path = Path(__file__).parent / 'json_data' / 'authors.json'
    quotes_path = Path(__file__).parent / 'json_data' / 'quotes.json'

    with open(quotes_path, 'r') as fh:
        quotes = json.load(fh)

    with open(author_path, 'r') as fh:
        authors = json.load(fh)
    tags = []
    for quote in quotes:
        tags.extend(quote.get('tags'))
    tags = set(tags)
    tags = list(tags)
    Tag.objects.all().delete()
    for _tag in tags:
        Tag.objects.create(name=_tag)

    Author.objects.all().delete()
    for author_ in authors:
        Author.objects.create(fullname=author_.get('fullname'),
                              born_date=author_.get('born_date'),
                              born_location=author_.get('born_location'),
                              description=author_.get('description'), )
    Quote.objects.all().delete()
    for quote_ in quotes:
        quote_temp = Quote.objects.create(quote=quote_.get('quote'),
                                          author=Author.objects.filter(fullname=quote_.get('author')).first())
        for tag_name in quote_.get('tags'):
            quote_temp.tags.add(Tag.objects.filter(name=tag_name).first())



