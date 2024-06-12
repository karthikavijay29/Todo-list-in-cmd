import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description="Command-line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear all tasks")
    return parser

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:  # Check if there are tasks
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found.")
    else:
        print("No tasks found.")

def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed successfully.")
    else:
        print("No tasks found.")

def clear_tasks():
    if os.path.exists("tasks.txt"):
        os.remove("tasks.txt")
        print("All tasks cleared.")
    else:
        print("No tasks found.")

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    elif args.clear:
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
