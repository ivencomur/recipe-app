from django.db import models

GENRE_CHOICES = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational'),
)

BOOK_TYPE_CHOICES = (
    ('hardcover', 'Hard cover'),
    ('ebook', 'E-Book'),
    ('audiobook', 'Audiobook'),
)

class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120)  # we’ll test this max_length later
    price = models.FloatField(help_text='in US dollars $')
    genre = models.CharField(max_length=12, choices=GENRE_CHOICES, default='classic')
    book_type = models.CharField(max_length=12, choices=BOOK_TYPE_CHOICES, default='hardcover')

    def __str__(self):
        return str(self.name)
