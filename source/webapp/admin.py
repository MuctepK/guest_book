from django.contrib import admin
from webapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'author_mail', 'text', 'status', 'created_at', 'updated_at']
    list_display_links = ['author_name']
    list_filter = ['status']
    search_fields = ['author_name', 'text']
    fields = ['author_name', 'author_mail', 'text', 'status']


admin.site.register(Note, NoteAdmin)