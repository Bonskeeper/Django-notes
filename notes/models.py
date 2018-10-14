# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Note(models.Model):
    """
    Model contains four fields. Field `title` - for note title. Field `content` - for note text.
    Field `date_posted` - when note created or modifaed. Field `unique_words_count` - the number
    of unique words in a note to sort notes
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    unique_words_count = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        This function return obsolute pass for template.
        """
        return reverse('note-detail', kwargs={'pk': self.pk})
