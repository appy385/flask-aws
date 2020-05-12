from app import *
from app.models import Books, BookTags
from app.globals import *
from app.helper import *
from sqlalchemy.sql.expression import func


@application.route('/')
def index():
    return "<h1>WELCOME TO FLASK-AWS APP!!</h1>"

#1 Get Books Recommendation on basis of genre
@application.route("/<genre>")
def genre(genre):
    # get goodreads_id of type genre="scifi/adventure/horror/..."
    book_tag = db.session.query(BookTags).filter_by(genre=genre).subquery()
    #join table Books with book_tag query table on basis of goodreads_id to get 10 random rows of particular genre
    result = db.session.query(Books,book_tag.c.genre).join(book_tag,Books.goodreads_book_id == book_tag.c.goodreads_book_id).order_by(func.rand()).limit(10).all()
    return books(result)

#2 Send feedback
@application.route('/contact',methods = ['POST'])
def contact():
        print(request);
        send_message(request.json,mail)
        return {
            "status": {"code": 200}
        }

#3 Get book Recommendation on basis of your goodreads id/username
@application.route('/goodreads_id/<username>')
def goodreads(username):
    uri = goodreads_url + username
    response = sendRequest(uri,params)

    if response.status_code==200:
        return parseXML(response)

    elif response.status_code==401:
        error = { 'status': { 'code': response.status_code }, 'error_message' : 'Unauthorized access.Please Try again!' }
        return error

    else:
        error = { 'status': { 'code': response.status_code }, 'error_message' : 'Goodreads User ID does not exist' }
        return error


#4 Get book Recommendation on basis of a book you enter
@application.route('/bookname/<booktitle>')
def booktitle(booktitle):
    return "hello"


if __name__ == "__main__":
     application.run(host ='0.0.0.0')
