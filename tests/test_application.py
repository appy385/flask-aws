from application import application, db
from app.models import Books , BookTags
import json
from io import BytesIO
import pytest


#Unit tests

def test_index():
    response = application.test_client().get('/')

    assert response.status_code == 200
    assert response.data ==  b"Congratulations!! TO FLASK-AWS APP"


def test_genre():
    response = application.test_client().get('/genre/scifi')
    bookstr = str(response.data , 'utf-8')
    li = list(bookstr.split("{}"))
    print (li)

    assert response.status_code == 200
    assert len(li) == 1


def test_popular():
    response = application.test_client().get('/popular')
    assert response.status_code == 200