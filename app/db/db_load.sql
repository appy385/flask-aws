LOAD DATA LOCAL INFILE '/Users/apoorva/Documents/ACMS/flask-sample/csv/books.csv'
INTO TABLE books
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(book_id, goodreads_book_id, authors, isbn, title, average_rating, image_url);

LOAD DATA LOCAL INFILE '/Users/apoorva/Documents/ACMS/flask-sample/csv/genre.csv'
INTO TABLE book_tags
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(book_tag_id, goodreads_book_id, genre);
