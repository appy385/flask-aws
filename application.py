from app import *
from app.models import Books, BookTags
from app.helper import *
from sqlalchemy.sql.expression import func


@application.route('/')
def index():
    return "<h1>Congratulations!!WELCOME TO FLASK-AWS APP!!</h1>"


@application.route("/<genre>")
def genre(genre):
    book_tag = db.session.query(BookTags).filter_by(genre=genre).subquery()
    result = db.session.query(Books,book_tag.c.genre).join(book_tag,Books.goodreads_book_id == book_tag.c.goodreads_book_id).order_by(func.rand()).limit(10).all()
    return books(result)

if __name__ == "__main__":
     application.run(host ='0.0.0.0')
