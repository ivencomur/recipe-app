from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            name='Pride and Prejudice',
            author_name='Jane Austen',
            genre='classic',
            book_type='hardcover',
            price=23.71,
        )

    def test_name_label(self):
        field_label = self.book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        max_length = self.book._meta.get_field('author_name').max_length
        self.assertEqual(max_length, 120)

    def test_defaults_when_not_provided(self):
        b = Book.objects.create(name='Defaulted', author_name='Anon', price=1.0)
        self.assertEqual(b.genre, 'classic')
        self.assertEqual(b.book_type, 'hardcover')

    def test_str_returns_name(self):
        self.assertEqual(str(self.book), 'Pride and Prejudice')

    def test_price_help_text_mentions_usd(self):
        help_text = self.book._meta.get_field('price').help_text
        self.assertIn('US dollars', help_text)
