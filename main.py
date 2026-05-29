class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added successfully.")
        else:
            print(f"Task '{task_name}' already exists.")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def mark_task_as_done(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as done.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def mark_task_as_undone(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' marked as undone.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def view_tasks(self):
        for task, status in self.tasks.items():
            if status:
                print(f"[X] {task}")
            else:
                print(f"[ ] {task}")


todo_list = ToDoList()

while True:
    print("\n1. Qo'shish")
    print("2. O'chirish")
    print("3. Qilgan")
    print("4. Qilmas")
    print("5. Ko'rish")
    print("6. Chiqish")

    choice = input("Izoh: ")

    if choice == "1":
        task_name = input("Task nomi: ")
        todo_list.add_task(task_name)
    elif choice == "2":
        task_name = input("Task nomi: ")
        todo_list.remove_task(task_name)
    elif choice == "3":
        task_name = input("Task nomi: ")
        todo_list.mark_task_as_done(task_name)
    elif choice == "4":
        task_name = input("Task nomi: ")
        todo_list.mark_task_as_undone(task_name)
    elif choice == "5":
        todo_list.view_tasks()
    elif choice == "6":
        break
    else:
        print("Izoh: Xato tanlov.")
```

Bu kodda biz To-Do ro'yxatini yaratish uchun `ToDoList` klassidan foydalanamiz. Ushbu klassda biz vazifalarni qo'shish, o'chirish, qilganlik holatini o'zgartirish va vazifalarni ko'rish uchun metodlar yaratdik.
