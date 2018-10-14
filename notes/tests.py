from django.test import TestCase
from .models import Note


class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Note.objects.create(title='this is test one note', content='this is my first test note', unique_words_count=6)
        Note.objects.create(title='this is test second note',
                            content='this is my second test note with more unique words', unique_words_count=10)

    def test_count_unique_wordsl(self):
        note_one = Note.objects.get(id=1)
        note_two = Note.objects.get(id=2)
        field_unique_words_count_note_one = note_one.unique_words_count
        field_unique_words_count_note_two = note_two.unique_words_count
        test_case = field_unique_words_count_note_one < field_unique_words_count_note_two
        self.assertTrue(test_case)
