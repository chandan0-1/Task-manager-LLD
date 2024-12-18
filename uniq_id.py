import uuid

class UniqId:
    def __init__(self):
        pass

    def getId(self):
        return uuid.uuid4().hex