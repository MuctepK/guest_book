from django.shortcuts import render, redirect
from webapp.models import Note, DEFAULT_STATUS
from webapp.forms import NoteForm


def index_view(request):
    notes = Note.objects.all().filter(status=DEFAULT_STATUS).order_by('-created_at')
    context = {'notes': notes}
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
    pass


def note_update_view(request, pk):
    pass