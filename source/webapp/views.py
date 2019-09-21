from django.shortcuts import render
from webapp.models import Note, DEFAULT_STATUS


def index_view(request):
    notes = Note.objects.all().filter(status=DEFAULT_STATUS).order_by('-created_at')
    context = {'notes': notes}
    return render(request, 'index.html', context)


def note_create_view(request):
    pass


def note_delete_view(request, pk):
    pass


def note_update_view(request, pk):
    pass