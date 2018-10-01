from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)  # success! return 200
    assert_in(b"Fill out this", rv.data)  # looks like substring is fine

    data = {'name': 'peppapig', 'greet': 'Aiya'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"peppa", rv.data)  # looks like substring is fine
    assert_in(b"Ai", rv.data)  # looks like substring is fine
