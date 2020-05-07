

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
    return booksDict
