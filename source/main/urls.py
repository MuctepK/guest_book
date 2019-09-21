from django.contrib import admin
from django.urls import path
from webapp.views import index_view, note_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('note/add', note_create_view, name='note_create')
]
