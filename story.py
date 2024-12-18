class Story:
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.tasks = []
        self.subtasks = []

    def addTask(self, task):
        if not task:
            print('Not a valid Task')
            return
        
        self.tasks.append(task)

    def addBulkTasks(self, tasks = []):
        self.tasks += tasks

    def addSubtask(self, subtask):
        if not subtask:
            print('Not a valid Subtask')
            return
        
        self.subtasks.append(subtask)

    def addBulkSubtasks(self, subtasks = []):
        self.subtasks += subtasks