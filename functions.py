
FILEPATH = 'todos.txt'
def get_todos(filepath = FILEPATH): # this helps set a default parameter
    """ Read a text file and return the list of 
    to-do items.
    """
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath =  FILEPATH):
    """ Writing the to do items list in the text file."""
    
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
    # return todos

print(__name__)
## Use this kindof reasoning when you want to only print todos.
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

    