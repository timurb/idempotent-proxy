from object_storage import *


def test_id_for():
    storage = ObjectStorage()
    assert storage.id_for('foobar') is not None
    assert storage.id_for(123) is not None
    assert storage.id_for([123]) is not None
    assert storage.id_for({'a': 'b'}) is not None

# Empty method as of now
def test_validate():
    storage = ObjectStorage()
    assert storage.is_valid('foo') is True
    assert storage.is_valid(1) is True
    assert storage.is_valid([]) is True
    assert storage.is_valid({}) is True

def test_get_empty():
    storage = ObjectStorage()
    assert storage.get(1) is None


def test_check():
    storage = ObjectStorage()
    objid = storage.put('foobar')
    assert storage.check('foobar') is not None
    assert storage.check('foobarzed') is None


def test_put():
    storage = ObjectStorage()
    objid = storage.put('foobar')
    assert storage.get(objid) == 'foobar'


def test_put_uses_object_id():
    storage = ObjectStorage()
    storage.put('foobar')
    objid = storage.id_for('foobar')
    assert storage.get(objid) == 'foobar'


def test_put_doesnt_shadow_each_other():
    storage = ObjectStorage()
    storage.put('foobar')
    storage.put('foobarzed')
    assert storage.get(storage.id_for('foobar')) == 'foobar'
    assert storage.get(storage.id_for('foobarzed')) == 'foobarzed'


def test_generate_id_for_object_is_not_none():
    storage = ObjectStorage()
    assert storage.id_for('foobar') is not None


def test_generate_id_for_object_is_unique():
    storage = ObjectStorage()

    id1 = storage.id_for('foobar')
    id2 = storage.id_for('foobarz')
    id3 = storage.id_for('foobar')
    assert id1 != id2
    assert id1 == id3
