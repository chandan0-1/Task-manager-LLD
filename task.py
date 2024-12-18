from subtask import Subtask
from uniq_id import UniqId

class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.subtasks = []

    def addSubtasks(self, subtask):
        self.subtasks.append(subtask)

    def createSubtask(self, name, description, id = None):
        if not name or len(name) < 5:
            print('--------- Name should have at least 5 characters --------')
            return None
        
        id = id or UniqId().getId()
        subtask = Subtask(id, name, description)
        self.addSubtasks(subtask)

        return subtask

    def displaySubtasks(self):
        print('                           --------------------------')
        print('                           SubTask details for {}'.format(self.name))
        print('                           __________________________')
        for subtask in self.subtasks:
            print(subtask)
        print()

    def __str__(self):
        return 'Id: {} \nName: {} \nDescription: {}\n'.format(self.id, self.name, self.description)