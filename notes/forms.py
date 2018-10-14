# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Note


class NoteForm(ModelForm):
    """
    This class contain class with instructions that are used to build the form in template.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        labels = {
            'title': _('Note title'),
            'content': _('Note text')
        }
