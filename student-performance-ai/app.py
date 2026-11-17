import streamlit as st

#Page configuration
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓"
)

#Application title
st.title("🎓 Student Performance AI")
#introductin
st.write("Welcome to Student Performance AI!")
st.subheader("Predict Student Performace")

#Display a message
st.info("Our AI model will help prdict student marks.")

#input field
study_hours= st.number_input(
    "Enter Study Hours:",
    min_value= 0.0,
    max_value=24.0,
    value= 2.0
)

#Display entered value
st.write("Study Hours:",study_hours)

attendence= st.number_input(
    "Enter Attendence Precentage:",
    min_value= 0,
    max_value= 100,
    value= 75
)

st.write("Attendence:",attendence,"%")

#button
if st.button("Submit Student Details"):
    st.success("Student details submitted successfully!")

    st.write("Study Hours:",study_hours)
    st.write("Attendence:",attendence,"%")