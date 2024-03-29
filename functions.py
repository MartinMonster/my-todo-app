FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads the file and puts each line as an item in the list 'todos'"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def store_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print('hello')
    print(get_todos())