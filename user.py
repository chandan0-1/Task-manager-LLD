class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.tasks = []
        self.stories = []

    def addTask(self, task):
        self.tasks.append(task)

    def displayAllTasks(self):
        print('             ...............................................')
        print('             Task Details for => {} | {}'.format(self.name, self.email))
        print('             ...............................................\n')
        for task in self.tasks:
            print(task)
            print()

    def addStory(self, story):
        self.stories.append(story)

    def displayAllStory(self):
        print('             ...............................................')
        print('             Task Details for => {} | {}'.format(self.name, self.email))
        print('             ...............................................\n')
        for task in self.tasks:
            print(task)
            print()

    def __str__(self):
        return '{} | {} | {}'.format(self.id, self.name, self.email)
