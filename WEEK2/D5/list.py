import streamlit as st
import pandas as pd
import httpx

st.title("Student Names")

student_names = []
student_classes = []

student = 0

while student < 5:
    name = st.text_input(
        f"Enter student name",
        key=f"name_{student}"
    )

    student_class = st.text_input(
        f"Enter student class",
        key=f"class_{student}"
    )

    student_names.append(name)
    student_classes.append(student_class)

    student += 1

df = pd.DataFrame({
    "Student Name": student_names,
    "Class": student_classes
})

st.write(df)

if st.button("Get Students"):
    try:
        response = httpx.get("http://localhost:8000/students")
        response.raise_for_status()
        st.session_state['api_students'] = response.json()
        
    except Exception as e:
        st.error(f"Failed to load students: {e}")

if 'api_students' in st.session_state and st.session_state.api_students:
    st.subheader("Students from FastAPI")
    api_df = pd.DataFrame(st.session_state.api_students)
    
    if 'name' in api_df.columns and 'class' in api_df.columns:
        api_df = api_df.rename(columns={"name": "Student Name", "class": "Class"})
    
    st.dataframe(api_df)
