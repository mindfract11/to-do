class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
    def complete(self):
        self.completed = True
    def show(self):
        if self.completed:
            print(f"[x] {self.title}")
        else:
            print(f"[ ] {self.title}")

class Manager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))
    def show_tasks(self):
        for task in self.tasks:
            task.show()
    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break



manager = Manager()

manager.add_task("Learn Python")
manager.add_task("Go to gym")
manager.show_tasks()
manager.complete_task("Learn Python")
manager.show_tasks()
manager.remove_task("Go to gym")
manager.show_tasks()
