import hashlib
import json


class ObjectStorage:
    def __init__(self):
        self.objects = {}
        pass

    # Put object to storage
    def put(self, obj):
        self.objects[self.id_for(obj)] = obj
        return self.id_for(obj)

    # Get object from storage by id
    def get(self, object_id):
        try:
            result = self.objects[object_id]
        except KeyError:
            result = None
        return result

    # Check if there is object passed as a param in storage
    def check(self, obj):
        return self.get(self.id_for(obj))

    # Get id for given object
    @staticmethod
    def id_for(obj):
        return hashlib.sha1(json.dumps(obj, sort_keys=True)).hexdigest()

    # Check if there is object passed as a param in storage
    def check(self, obj):
        return self.get(self.id_for(obj))

    # Check if object can be processed.
    # Dummy method as of now
    @staticmethod
    def is_valid(obj):
        return True
