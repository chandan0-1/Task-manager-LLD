class Subtask:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return 'Id: {} | Name: {} | Description: {}'.format(self.id, self.name, self.description)
