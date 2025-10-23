import streamlit as st
from datetime import date
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from Backend import LabFile

# Set page configuration
st.set_page_config(page_title="Lab Assignment Generator", layout="centered")

# Title
st.title("Lab Assignment Generator")

# Student Name
student_name = st.text_input("Student Name", placeholder="Enter your full name")

# AUD Number
aud_number = st.text_input("AUD Number", placeholder="Enter your AUD number")

# Subject Selection
subject = st.selectbox("Subject", ["Python", "Algorithms"])

# Lab Number
lab_number = st.text_input("Lab Number", placeholder="Enter lab number (e.g., 5)")

# Lab Date
lab_date = st.date_input("Lab Date", value=date.today())

# Questions
questions = st.text_area("Questions", placeholder="Enter the lab questions here...", height=200)

# Output Format Selection
output_format = st.radio("Select Output Format", ["Word", "PDF"])

# Submit Button
if st.button("Generate Lab Document"):
    # Validation
    if not lab_number:
        st.error("Please enter the lab number")
    elif not questions:
        st.error("Please enter the questions")
    else:
        # Display entered information
        st.write("---")
        st.write("**Summary:**")
        st.write(f"- **Name:** {student_name}")
        st.write(f"- **AUD Number:** {aud_number}")
        st.write(f"- **Subject:** {subject}")
        st.write(f"- **Lab Number:** {lab_number}")
        st.write(f"- **Lab Date:** {lab_date}")
        st.write(f"- **Output Format:** {output_format}")
        
        # Generate the document
        with st.spinner(f"Generating {output_format} document..."):
            try:
                question_list = [q.strip() for q in questions.split("\n") if q.strip()]
                filename = LabFile.create_python_lab_file(
                    student_name, 
                    aud_number, 
                    lab_number, 
                    question_list
                )
                
                st.success(f"✅ Document generated successfully!")
                
                # Provide download button
                with open(filename, "rb") as file:
                    st.download_button(
                        label=f"📥 Download {output_format} Document",
                        data=file,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    
            except Exception as e:
                st.error(f"❌ Error generating document: {str(e)}")
                st.exception(e)

