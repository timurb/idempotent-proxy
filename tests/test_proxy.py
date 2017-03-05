import json

import responses

from proxy import *


@responses.activate
def test_get():
    responses.add(responses.GET, 'http://www.google.com/foo/bar', body='ok')
    proxy = ApiProxy('http://www.google.com/foo/bar')

    proxy.get()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://www.google.com/foo/bar'


@responses.activate
def test_post():
    responses.add(responses.POST, 'http://www.google.com/foo/bar', body='ok')
    proxy = ApiProxy('http://www.google.com/foo/bar')

    proxy.post({'foo': 'bar'})

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://www.google.com/foo/bar'
    assert json.loads(responses.calls[0].request.body) == {'foo': 'bar'}


@responses.activate
def test_put():
    responses.add(responses.PUT, 'http://www.google.com/foo/bar', body='ok')
    proxy = ApiProxy('http://www.google.com/foo/bar')

    proxy.put({'foo': 'bar'})

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://www.google.com/foo/bar'
    assert json.loads(responses.calls[0].request.body) == {'foo': 'bar'}


@responses.activate
def test_delete():
    responses.add(responses.DELETE, 'http://www.google.com/foo/bar', body='ok')
    proxy = ApiProxy('http://www.google.com/foo/bar')

    proxy.delete()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://www.google.com/foo/bar'
