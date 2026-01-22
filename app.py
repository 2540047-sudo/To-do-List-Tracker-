import streamlit as st

# Title
st.title("📝 To-Do List Tracker")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
task = st.text_input("Enter a new task:")

# Add button
if st.button("Add Task"):
    if task != "":
        st.session_state.tasks.append(task)
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.write("---")

# Display tasks
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet.")
else:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4,1])
        col1.write(f"{i+1}. {t}")
        if col2.button("Delete", key=i):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
