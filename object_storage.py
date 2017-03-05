class ObjectStorage:
    def __init__(self):
        self.objects = {}
        pass

    def put(self, object_id, object):
        self.objects[object_id] = object

    def get(self, object_id):
        try:
            result = self.objects[object_id]
        except KeyError:
            result = None
        return result
