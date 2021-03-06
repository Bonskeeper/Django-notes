# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from .models import Note
from .forms import NoteForm


def about(request):
    """
    Display the application information.
    """
    return render(request, 'notes/about.html', {'title': 'About'})


class NoteListView(ListView, FormView):
    """
    Display a form for notes as well as notes sorted by unique words.
    """
    model = Note
    form_class = NoteForm
    template_name = 'notes/home_form.html'
    context_object_name = 'notes'
    ordering = ['-unique_words_count']
    paginate_by = 3

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.unique_words_count = len(set(form.instance.content.split(' ')))
        instance.save()
        return redirect(reverse_lazy('note-detail', args=[instance.pk]))


class NoteDetailView(DetailView):
    """
    Display the details of the selected note..
    """
    model = Note


class NoteUpdateView(UpdateView):
    """
    Display update selected note form.
    """
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.unique_words_count = len(set(form.instance.content.split(' ')))
        return super().form_valid(form)


class NoteDeletelView(DeleteView):
    """
    Display confirmation message to delete selected note.
    """
    model = Note
    success_url = '/'
