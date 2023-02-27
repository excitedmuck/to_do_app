import streamlit as st
import functions

todos =  functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append("\n"+todo)
    functions.write_todos(todos)
    print(todo)

st.title("My Todo App")    
st.subheader("Yashvini on steroids.")

st.write("This app will increase your productivity. ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox (todo, key = index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()


st.text_input(label = "Enter a todo:", placeholder= "Add a new todo...", 
            on_change=add_todo, key ='new_todo')

st.session_state