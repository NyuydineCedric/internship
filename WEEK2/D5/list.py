import streamlit as st
import pandas as pd

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