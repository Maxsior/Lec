class UnknownObjectError(Exception):
    def __init__(self, id):
        self.object_id = id

    def __str__(self):
        return f"Can't find definition of object '{self.object_id}'"
