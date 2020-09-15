import pytest

def test_default_route(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data.decode('utf-8') == 'success!!!'


def test_contactDone(client):
    res = client.get('/contact-done')
    assert res.status_code == 200
    assert 'Thanks for contacting us !!!' in res.data.decode('utf-8')

def test_formLoaded(client):
    res = client.get('/process-contact-form')
    assert res.status_code == 200
    assert 'emaildjjd' in res.data.decode('utf-8')
    assert 'namejehdn' in res.data.decode('utf-8')
    assert 'subjectjdhf' in res.data.decode('utf-8')
    assert 'messagejdjkdkd' in res.data.decode('utf-8')
    assert 'email' in res.data.decode('utf-8')
    assert 'name' in res.data.decode('utf-8')
    assert 'subject' in res.data.decode('utf-8')
    assert 'message' in res.data.decode('utf-8')

def test_honeypod(client):
    data = {
        'emaildjjd': 'aaa@aol.com',
        'namejehdn': 'Ahaorn Amed Aship',
        'subjectjdhf': 'Testing',
        'messagejdjkdkd': 'A message',
        'email': 'aaa@aol.com',
        'name': 'Ahaorn Amed Aship',
        'subject': 'Testing',
        'message': 'A message'
    }
    rv = client.post('/process-contact-form', data=data)
    assert rv.status_code == 400
    assert 'You are fishy' in rv.data.decode('utf-8')


def test_contact_make(client):
    from application.models import Contact

    data = {
        'emaildjjd': 'aaa@aol.com',
        'namejehdn': 'Ahaorn Amed Aship',
        'subjectjdhf': 'Testing',
        'messagejdjkdkd': 'A message',
    }
    rv = client.post(
        '/process-contact-form', data=data, follow_redirects=True)
    assert rv.status_code == 200
    assert 'Thanks for contacting us !!!' in rv.data.decode('utf-8')
    assert Contact.get('aaa@aol.com') is not None
