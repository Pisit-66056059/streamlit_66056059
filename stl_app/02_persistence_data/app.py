import streamlit as st

st.title('My To-Do List Creator')
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = [{"Learn Markdown": 1},
                                     {"Learn Python": 7},
                                     {"Learn Streamlit":5}]
#st.write('My current To-Do list is:', st.session_state.my_todo_list)

new_todo = st.text_input("What do you need to do?")
day_todo = st.number_input('How many days do you want to spare"',
                           min_value=1, max_value=10)

if st.button('Add the new To-Do item'):
    st.write('Adding a new item to the list')
    st.session_state.my_todo_list.append({new_todo: day_todo})

st.write('My new To-Do list is:', st.session_state.my_todo_list)

# Fixed
# 1. make it save to session state
#    https://docs.streamlit.io/library/api-reference/session-state
# 2. add a number input for number of day for each todo.
#    You may need to change the data structure of `my_todo_list`


