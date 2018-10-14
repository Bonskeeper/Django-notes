# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from .models import Note
from .forms import NoteForm


def about(request):
    """
    This view displays the application information.
    """
    return render(request, 'notes/about.html', {'title': 'About'})


class NoteListView(ListView, FormView):
    """
    This view displays a form for notes as well as notes sorted by unique words.
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
    This view displays the details of the selected note..
    """
    model = Note


class NoteUpdateView(UpdateView):
    """
    This view displays a form to update the selected note.
    """
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.unique_words_count = len(set(form.instance.content.split(' ')))
        return super().form_valid(form)


class NoteDeletelView(DeleteView):
    """
    This view displays a confirmation message to delete the selected note.
    """
    model = Note
    success_url = '/'
