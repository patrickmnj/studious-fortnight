import sqlite3

class TaskManager:
    def __init__(self, db_name = "group1.db"):
        self.db_name = db_name
   
    def get_connection(self):
        return sqlite3.connect("group1.db")
        
        # Create table
    def create_table(self):
        connection = self.get_conncetion() 
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                completed TEXT
            )
        """)

        connection.commit()
        connection.close()

class Task:
    def __init__(self, id=None, title="", description="", due_date="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed


    def add_task(self):
        connection = sqlite3.connect("group1.db",)
        cursor = connection.cursor()
#there was a comma in line 42 aftere the last question2
        cursor.execute("""
            INSERT INTO tasks (title, description, due_date)
            VALUES (?, ?, ?,)
        """, (
            self.title,
            self.description,
            self.due_date
        ))

        connection.commit()
        connection.close()
        
    def complete_task(self):
        task_id = input("Enter the ID of the task to complete: ")

        connection = sqlite3.connect("group1.db",)
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE tasks
            SET completed = 'Yes'
            WHERE id = ?
        """, (task_id,))

        connection.commit()
        connection.close()

        print ("Task marked as complte")

    def view_tasks(self):
        connection = sqlite3.connect("group1.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")
        all_tasks = cursor.fetchall()

        connection.commit()
        connection.close()
        return all_tasks

    def delete_task(self):
        connection = sqlite3.connect("group1.db", timeout=15)
        cursor = connection.cursor()

        cursor.execute(f"""
            DELETE FROM tasks WHERE title = '{self.title}'
        
        """)
        connection.commit()
        connection.close()

def main():
    while True:
        print("\n___ Task Manager ___")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")

            task = Task(
                title=title,
                description=description,
                due_date=due_date
        )

            task_t= task.add_task()
            print(task_t)
            print("Task added successfully")

        elif choice == "2":

            t_add = Task().view_tasks()
            for data in t_add:
                print(data) 

            

        elif choice == "3":
            title = input("Enter the tittle you want to complete:")
            task =Task()
            task.complete_task()
            print("Completed")

        elif choice == "4":
            title = input("Enter the title you would want to delete:")
            delete_task = Task(title=title)
            delete_task.delete_task()
            print(delete_task)
        
        elif choice == "5":
            print("Adios!")
            break

        else:
            print("Invalid choice. Try again")

main()