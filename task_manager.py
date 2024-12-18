from user import User
from task import Task
from uniq_id import UniqId
from subtask import Subtask

class TaskManager:
    def __init__(self):
        self.current_user = None
        self.users = {}

    # ------------------------------------------------------
    # ----------------- User section -----------------------
    # ------------------------------------------------------
    def loginUser(self, email, password):
        if self.current_user:
            print('---------------------------------------')
            print('---- Below User is already loggedin please logout first ----')
            print(self.current_user)
            print('------------------')
            return 
        
        user = self.users.get(email)
        if not user:
            print('---------- Invalid email Provided ---------------')
            return

        if user.email != email or user.password != password:
            print('---------- Invalid email or password ---------------')
            return

        print('\n-------------------- User Login Successful ---------------------')
        self.current_user = user
        print(self.current_user)
        print('----------------------------------------------------------------\n')

    # @params id               Uniq id
    # @params name             User's Name
    # @params email            User's Email
    # @params password         User's Password
    def createUser(self, name, email, password, id = None):
        if not email or not password:
            print('------ Email or password is Invalid -----------')
            return

        if len(email) < 4 or len(password) < 4:
            print('--------- Email and password length should be 4 character --------')
            return

        if self.users.get(email):
            print('-------- User email is already Taken --------------')
            return

        uniq_id = id or self.getUniqId()
        user = User(uniq_id, name, email, password)
        self.addUser(user)
        
        print()
        print('User created => {} | {}'.format(user.name, user.email))
        print()
        
        return user
    

    def addUser(self, user):
        self.users[user.email] = user


    def logoutUser(self):
        if not self.current_user:
            print('--------- No user is loggedin currently ----------')
            return
        
        print('\n------------------- User logged out Successfully ---------------------')
        print(self.current_user)
        self.current_user = None
        print('----------------------------------------------------------------------\n')

    def showAllTasksForLoggedinUser(self):
        self.current_user.displayAllTasks()
    

    # ------------- Tasks Managment -----------------
    def createTask(self, name, description, id = None):
        if not name or len(name) < 5:
            print('--------- Name should have at least 5 characters --------')
            return
        id = id or self.getUniqId()
        task = Task(id, name, description)
        return task

    def getUniqId(self):
        return UniqId().getId()

    def initProgram(self):
        print('---------- Program started --------------------')
        u1 = self.createUser('Ravi', 'ravi@gmail.com', 'ravi@123')
        u2 = self.createUser('Ravi', 'ravi@gmail.com', 'r')
        u3 = self.createUser('Chandan', 'chandan@gmail.com', 'chandan@123')
        u4 = self.createUser('Test', 'test@gmail.com', 'test', 4)

        t1 = self.createTask('Task 1', 'Task Description 1', 1)
        t2 = self.createTask('Task 2', 'Task Description for task 2')
        t3 = self.createTask('Task 3', 'Task Description for tasksdkjgh')
        t4 = self.createTask('Task 4', 'Task Description for task 4')

        st1 = t1.createSubtask('SubTask 1', 'SubTask Description 1')
        st2 = Subtask(2, 'SubTask 2', 'SubTask Description for subtask2')
        st3 = t2.createSubtask('SubTask 3', 'SubTask Description for subtask3')
        
        t2.addSubtasks(st2)
        t4.addSubtasks(st3)
        t3.addSubtasks(st3)

        u1.addTask(t1)
        u1.addTask(t3)
        u1.addTask(t4)
        u3.addTask(t2)
        u3.addTask(t4)

        t1.addSubtasks(st1)

        self.logoutUser()
        self.loginUser('asadad', 'assad@gmail.com')
        self.loginUser('chandan@gmail.com', 'chandan@123')
        self.showAllTasksForLoggedinUser()

        t1.displaySubtasks()

        u1.displayAllTasks()
        self.logoutUser()

        

taskManager = TaskManager()
taskManager.initProgram()

    

    