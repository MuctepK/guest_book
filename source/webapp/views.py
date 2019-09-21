from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Note, DEFAULT_STATUS
from webapp.forms import NoteForm, SearchForm


def index_view(request):
    notes = Note.objects.all().filter(status=DEFAULT_STATUS).order_by('-created_at')
    search_form = SearchForm()
    context = {'notes': notes, 'search_form': search_form}
    return render(request, 'index.html', context)


def note_create_view(request):
    if request.method == 'GET':
        form = NoteForm()
        return render(request, 'create.html', context=
        {
            'form': form
        })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'create.html', context={'form': form})
        Note.objects.create(author_name=form.cleaned_data['author_name'],
                            author_mail=form.cleaned_data['author_mail'],
                            text=form.cleaned_data['text'])
        return redirect('index')


def note_delete_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'note': note})
    elif request.method == 'POST':
        note.delete()
        return redirect('index')


def note_update_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(data={'author_name': note.author_name,
                              'author_mail': note.author_mail,
                              'text': note.text})
        return render(request, 'update.html', context={'note': note,
                                                       'form': form
                                                       })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.author_name = form.cleaned_data['author_name']
            note.author_mail = form.cleaned_data['author_mail']
            note.text = form.cleaned_data['text']
            note.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={
                'form': form, 'note': note
            })


def note_search_view(request):
    pattern = request.GET.get('pattern')
    notes = Note.objects.all().filter(author_name__icontains=pattern)
    search_form = SearchForm()
    context = {'notes': notes, 'search_form': search_form}
    return render(request, 'index.html', context)