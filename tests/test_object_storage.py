from object_storage import *


def test_get_empty():
    storage = ObjectStorage()
    assert storage.get(1) is None


def test_set_get():
    storage = ObjectStorage()
    storage.put(1, 'foobar')
    assert storage.get(1) == 'foobar'
