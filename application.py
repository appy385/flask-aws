from app import *
from app.models import Books, BookTags
from app.globals import *
from app.helper import *
from sqlalchemy.sql.expression import func
import os
import pandas as pd
import json
path = os.path.abspath(os.path.dirname(__file__))

@application.route('/')
def index():
    return "Congratulations!! TO FLASK-AWS APP"


#1 Get Books Recommendation on basis of genre
@application.route("/genre/<genre>")
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

#Send all book titles from book.csv
@application.route('/title')
def bookTitle():
    df = pd.read_csv(path +'/csv/books.csv')
    df.dropna(subset=['title'],inplace=True)
    book_titles = df['title'].tolist()
    return {"titles":book_titles}

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


#4 Get book Recommendation on basis of a bookname you enter
@application.route('/recommend/booktitle/<bookname>', methods=['POST', 'GET'])
def recommendations_on_book_title(bookname):
    #Hound of the Baskervilles
    booktitle = ''
    if request.method=='POST':
        booktitle = request.json['inputtitle']
    else:
        booktitle = bookname
    uri = test_goodreads_url + booktitle
    response = sendRequest(uri,test_params)
    if response.status_code==200:
        return parseXML1(response)

    else:
        error = { 'status': { 'code': response.status_code }, 'error_message' : 'This bookname does not exist in goodreads' }
        return error


#5 Get Popular Books
@application.route('/popular')
def popularBooks():
    path = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(path +'/csv/books.csv')
    df.dropna(subset=['original_title'],inplace=True)
    df['weighted_rating'] = df['average_rating']*df['ratings_count']
    df.sort_values('weighted_rating',ascending=False,inplace=True)
    df = df[:24]
    df=df.sample(frac=0.5)
    df=df[['goodreads_book_id', 'authors', 'isbn', 'title', 'average_rating', 'image_url']]
    result= df.to_json(orient='records')
    return result


#5 Update average rating and count
@application.route('/rating', methods=['POST'])
def ratings():
    if request.method=='POST':
        isbn = int(request.json['isbn'])
        rating = int(request.json['rating'])
        book = db.session.query(Books).filter_by(isbn=isbn).all()
        book[0].average_rating = ( book[0].average_rating*book[0].ratings_count + rating ) / (book[0].ratings_count +1)
        book[0].ratings_count = book[0].ratings_count + 1;
        db.session.commit()
        return "Rated sucessfully"

    error = {  'error_message' : 'Unscuccessful attempt to rate book' }
    return error



if __name__ == "__main__":
     application.run(host ='0.0.0.0')
