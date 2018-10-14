# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .views import NoteListView, NoteDetailView, NoteUpdateView, NoteDeletelView

urlpatterns = [
    path('', NoteListView.as_view(), name="notes-home"),
    path('note/<int:pk>/', NoteDetailView.as_view(), name="note-detail"),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name="note-update"),
    path('note/<int:pk>/delete/', NoteDeletelView.as_view(), name="note-delete"),
    path('about/', views.about, name="notes-about"),
]
