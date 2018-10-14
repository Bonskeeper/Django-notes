# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Note


class NoteForm(ModelForm):
    """
    Build form from Note model. Allow editing of `title` and `content` fields.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        labels = {
            'title': _('Note title'),
            'content': _('Note text')
        }
