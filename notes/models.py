# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Note(models.Model):
    """
    This class contains the parameters that are used to build the model.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    unique_words_count = models.IntegerField()

    def __str__(self):
        """
        This function displays the model name.
        """
        return self.title

    def get_absolute_url(self):
        """
        This function return obsolute pass for template.
        """
        return reverse('note-detail', kwargs={'pk': self.pk})
