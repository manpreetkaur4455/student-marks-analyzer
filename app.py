import streamlit as st
import pandas as pd

# App Title
st.title("📊 Student Marks Analyzer")

# Student Name Input
student_name = st.text_input("Enter Student Name")

# Subject Marks Input
subject1 = st.number_input(
    "Enter marks for Subject 1",
    min_value=0,
    max_value=100
)

subject2 = st.number_input(
    "Enter marks for Subject 2",
    min_value=0,
    max_value=100
)

subject3 = st.number_input(
    "Enter marks for Subject 3",
    min_value=0,
    max_value=100
)

# Calculate Button
if st.button("Calculate Result"):

    # Calculate Total and Average
    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3

    # Grade Calculation
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display Student Results
    st.subheader("📌 Student Result")
    st.write("Student Name:", student_name)
    st.write("Total Marks:", total_marks)
    st.write("Average Marks:", round(average_marks, 2))
    st.write("Grade:", grade)

    # Create DataFrame
    marks_data = pd.DataFrame({
        "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [subject1, subject2, subject3]
    })

    # Display Table
    st.subheader("📋 Marks Table")
    st.dataframe(marks_data)

    # Bar Chart
    st.subheader("📊 Marks Comparison")
    st.bar_chart(marks_data.set_index("Subjects"))

    # Line Chart
    st.subheader("📈 Marks Trend")
    st.line_chart(marks_data.set_index("Subjects")) 
