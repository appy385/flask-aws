from app.models import *

def test_book():
    """
    GIVEN a Books model
    WHEN a new Book is created
    THEN check the goodreads_book_id  and average_rating
    """
    book = Books(goodreads_book_id=17332218,authors='Brandon Sanderson',isbn='765326361',title='Words of Radiance',average_rating=4.77,image_url='https://images.gr-assets.com/books/1391535251m/17332218.jpg',ratings_count=73572)
    assert book.goodreads_book_id == 17332218
    assert book.average_rating == 4.77


def test_book_tag():
    """
    GIVEN a BookTags model
    WHEN a new Book_tag is created
    THEN check the goodreads_book_id and genre is in the list of genre

    """
    genre = ['scifi','adventure','horror','comedy','poetry','romance','bio']

    book_tag = BookTags(goodreads_book_id=17332218,genre='scifi')

    assert book_tag.goodreads_book_id == 17332218
    assert (book_tag.genre in genre) == True
