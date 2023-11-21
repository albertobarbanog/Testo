def get_todos(filepath='files/todos.txt'):
    """Reads todos from file and returns them as a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='files/todos.txt'):
    """Writes todos to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

