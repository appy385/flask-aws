import json
import requests
import xml.etree.ElementTree as ElementTree

def sendRequest(uri,params):
        response = requests.get(uri,params)
        return response

def parseXML(res):
    book_list={}
    root = ElementTree.fromstring(res.content)
    for child in root.iter('update'):
        r=child.find('action')
        if r is None:
            continue
        goodreads_id = ((((child.find('object')).find('book')).find('id')).text)
        rating = (r.find('rating').text)
        book_list[goodreads_id]=rating

    return book_list

def send_message(message,mail):
    print(message['email'])
    msg = Message(subject="feedback for bookaholics", sender='contactbookaholics@gmail.com', recipients=['contactbookaholics@gmail.com'])
    msg.body = """
          From: %s <%s>
          %s
          """ % (message['name'], message['email'], message['message'])
    mail.send(msg)


def books(result):
    booksList=[]
    for b in result:
        book={}
        book['genre'] =  b.genre
        book['book_id'] = b[0].book_id
        book['goodreads_book_id'] = b[0].goodreads_book_id
        book['authors'] = b[0].authors
        book['isbn'] = b[0].isbn
        book['title'] = b[0].title
        book['average_rating'] = b[0].average_rating
        book['image_url'] = b[0].image_url
        booksList.append(book)

    booksDict={ "bookslist": booksList}
    booksDict = json.dumps(booksDict)
    booksJson = json.loads(booksDict)
    return booksJson
