# day15: добавление константы к описанию функций.
FILEPATH = 'todos.txt'

# day11: FUNCTIONS - very good explanation of print/return
# day12: functions with multiple parameters
# day13: default parameter
def get_todos(filepath=FILEPATH):
    """ This is a doc string. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# 2 break lines btwn functions
# day12: functions with multiple parameters
# day13: default parameter
# this function is more like a procedure, because does not return anything (only modifies the file). so we don't use RETURN
def write_todos(todo_arg, filepath=FILEPATH):
    """ Write a to-do items in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
        # None is an output for this function

# __name__  hidden variable
if __name__ == "__main__":
    # __name__ == "__main__" only if we execute the file directly
    print(f'We execute file directly. __name__ is now called "{__name__}"')
else:
    # __name__ == FILENAME if we execute file indirectly
    print(f'__name__ is now called "{__name__}" because we execute file indirectly')