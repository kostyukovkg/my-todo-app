import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'  # day19 session_state is a 'dictionary' with key 'new_todo'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ''


st.title('Simply the Best Todo App')
# st.subheader('This is my Todo App')
st.write('Please enter your todo items below')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # if checkbox is checked
        todos.pop(index)  # delete the item from todos
        functions.write_todos(todos)
        del st.session_state[todo]  # delete a todo from session state
        st.experimental_rerun()  # needed for checkboxes

st.text_input(label='', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')  # day19 при изменении поля ввода - вызывается функция add_todo