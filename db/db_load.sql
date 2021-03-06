LOAD DATA LOCAL INFILE '/Users/apoorva/Documents/AWS/flask-aws/csv/books_subset.csv'
INTO TABLE books
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(book_id, goodreads_book_id, authors, isbn, title, average_rating, image_url, ratings_count);

LOAD DATA LOCAL INFILE '/Users/apoorva/Documents/AWS/flask-aws/csv/genre.csv'
INTO TABLE book_tags
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(book_tag_id, goodreads_book_id, genre);
