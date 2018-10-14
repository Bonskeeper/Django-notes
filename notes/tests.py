from django.test import TestCase
from django.test.client import RequestFactory

from .models import Note
from .forms import NoteForm
from .views import NoteListView


class NoteModelTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        for number in range(5):
            Note.objects.create(title='Test note number {}'.format(number), content='Test note with six unique words',
                                unique_words_count=6)

    def test_results(self):
        """
        In `setUp` we create 5 note objects. We have a pagination of three notes
        on the page. By requesting the second page we must get status code 200
        """
        request = self.factory.get("/?page=2")
        response = NoteListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_valid_form(self):
        """
        Form validation test
        """
        data = {
            'title':'this is test one note',
            'content': 'this is my first test note',
        }
        form = NoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Negative form validation test
        """
        data = {
            'title':'this is test two note',
            'content': '',
        }
        form = NoteForm(data=data)
        self.assertFalse(form.is_valid())