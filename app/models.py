from app import db


class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    goodreads_book_id =  db.Column(db.Integer, unique = True)
    authors = db.Column(db.String(500), nullable = False)
    isbn = db.Column(db.String(255), nullable = False)
    title = db.Column(db.String(255), nullable = False)
    average_rating =  db.Column(db.Float, nullable = False)
    image_url = db.Column(db.String(255), nullable = False)

    def __repr__(self):
        return '<Book{}>'.format(self.title)


class BookTags(db.Model):
    book_tag_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    goodreads_book_id =  db.Column(db.Integer, db.ForeignKey('books.goodreads_book_id'))
    genre = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return '<BookTags{}>'.format(self.goodreads_book_id)
