from django.contrib import admin
from django.urls import path
from webapp.views import index_view, note_create_view, note_update_view, note_delete_view, note_search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('note/add', note_create_view, name='note_create'),
    path('note/update/<int:pk>/', note_update_view, name='note_update'),
    path('note/delete/<int:pk>/', note_delete_view, name='note_delete'),
    path('search/', note_search_view, name='note_search')
]
