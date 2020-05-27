from application import application
from app.models import Books , BookTags
import json
from io import BytesIO
import pytest

# 
# def test_index():
#     response = application.test_client().get('/')
#
#     assert response.status_code == 200
#     assert response.data ==  b"Congratulations!! TO FLASK-AWS APP"


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


def test_rating():
    with application.test_client() as c:
        response = c.post('/rating',json={'isbn':'765326361','rating':'4'})
        assert response.status_code == 200
