from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)  # success! return 200
    assert_in(b"Central Corridor", rv.data)  # looks like substring is fine

    data = {'action': 'tell a joke'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"Laser Weapon Armory", rv.data)

    data = {'action': '233'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"The Bridge", rv.data)

    data = {'action': 'slowly place the bomb'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"Escape Pod", rv.data)

    data = {'action': '2'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"The End", rv.data)
