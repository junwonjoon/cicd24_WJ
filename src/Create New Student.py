"""
This is a page 2
Author: Wonjoon Jun
Date: Jun 7, 2024
Please view README.md for more information.
"""
import streamlit as st
import os
import json

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("Create New Student")
user = st.text_input("Your Name", "FirstName LastName")
student_ID = st.text_input("Enter student ID")
courses_that_user_take = st.multiselect("Current courses that I take-", [
    "Language A - Literature (Afrikaans)",
    "Language A - Literature (Albanian)",
    "Language A - Literature (Amharic)",
    "Language A - Literature (Arabic)",
    "Language A - Literature (Armenian)",
    "Language A - Literature (Azerbaijani)",
    "Language A - Literature (Bengali)",
    "Language A - Literature (Bosnian)",
    "Language A - Literature (Bulgarian)",
    "Language A - Literature (Catalan)",
    "Language A - Literature (Chinese)",
    "Language A - Literature (Croatian)",
    "Language A - Literature (Czech)",
    "Language A - Literature (Danish)",
    "Language A - Literature (Dutch)",
    "Language A - Literature (English)",
    "Language A - Literature (Estonian)",
    "Language A - Literature (Filipino)",
    "Language A - Literature (Finnish)",
    "Language A - Literature (French)",
    "Language A - Literature (Georgian)",
    "Language A - Literature (German)",
    "Language A - Literature (Greek)",
    "Language A - Literature (Hebrew)",
    "Language A - Literature (Hindi)",
    "Language A - Literature (Hungarian)",
    "Language A - Literature (Icelandic)",
    "Language A - Literature (Indonesian)",
    "Language A - Literature (Italian)",
    "Language A - Literature (Japanese)",
    "Language A - Literature (Kazakh)",
    "Language A - Literature (Korean)",
    "Language A - Literature (Latvian)",
    "Language A - Literature (Lithuanian)",
    "Language A - Literature (Macedonian)",
    "Language A - Literature (Malay)",
    "Language A - Literature (Nepali)",
    "Language A - Literature (Norwegian)",
    "Language A - Literature (Persian)",
    "Language A - Literature (Polish)",
    "Language A - Literature (Portuguese)",
    "Language A - Literature (Romanian)",
    "Language A - Literature (Russian)",
    "Language A - Literature (Serbian)",
    "Language A - Literature (Sinhala)",
    "Language A - Literature (Slovak)",
    "Language A - Literature (Slovenian)",
    "Language A - Literature (Spanish)",
    "Language A - Literature (Swahili)",
    "Language A - Literature (Swedish)",
    "Language A - Literature (Tamil)",
    "Language A - Literature (Thai)",
    "Language A - Literature (Turkish)",
    "Language A - Literature (Ukrainian)",
    "Language A - Literature (Urdu)",
    "Language A - Literature (Vietnamese)",
    "Language A - Literature (Welsh)",
    "Language A - Language and Literature (Afrikaans)",
    "Language A - Language and Literature (Albanian)",
    "Language A - Language and Literature (Amharic)",
    "Language A - Language and Literature (Arabic)",
    "Language A - Language and Literature (Armenian)",
    "Language A - Language and Literature (Azerbaijani)",
    "Language A - Language and Literature (Bengali)",
    "Language A - Language and Literature (Bosnian)",
    "Language A - Language and Literature (Bulgarian)",
    "Language A - Language and Literature (Catalan)",
    "Language A - Language and Literature (Chinese)",
    "Language A - Language and Literature (Croatian)",
    "Language A - Language and Literature (Czech)",
    "Language A - Language and Literature (Danish)",
    "Language A - Language and Literature (Dutch)",
    "Language A - Language and Literature (English)",
    "Language A - Language and Literature (Estonian)",
    "Language A - Language and Literature (Filipino)",
    "Language A - Language and Literature (Finnish)",
    "Language A - Language and Literature (French)",
    "Language A - Language and Literature (Georgian)",
    "Language A - Language and Literature (German)",
    "Language A - Language and Literature (Greek)",
    "Language A - Language and Literature (Hebrew)",
    "Language A - Language and Literature (Hindi)",
    "Language A - Language and Literature (Hungarian)",
    "Language A - Language and Literature (Icelandic)",
    "Language A - Language and Literature (Indonesian)",
    "Language A - Language and Literature (Italian)",
    "Language A - Language and Literature (Japanese)",
    "Language A - Language and Literature (Kazakh)",
    "Language A - Language and Literature (Korean)",
    "Language A - Language and Literature (Latvian)",
    "Language A - Language and Literature (Lithuanian)",
    "Language A - Language and Literature (Macedonian)",
    "Language A - Language and Literature (Malay)",
    "Language A - Language and Literature (Nepali)",
    "Language A - Language and Literature (Norwegian)",
    "Language A - Language and Literature (Persian)",
    "Language A - Language and Literature (Polish)",
    "Language A - Language and Literature (Portuguese)",
    "Language A - Language and Literature (Romanian)",
    "Language A - Language and Literature (Russian)",
    "Language A - Language and Literature (Serbian)",
    "Language A - Language and Literature (Sinhala)",
    "Language A - Language and Literature (Slovak)",
    "Language A - Language and Literature (Slovenian)",
    "Language A - Language and Literature (Spanish)",
    "Language A - Language and Literature (Swahili)",
    "Language A - Language and Literature (Swedish)",
    "Language A - Language and Literature (Tamil)",
    "Language A - Language and Literature (Thai)",
    "Language A - Language and Literature (Turkish)",
    "Language A - Language and Literature (Ukrainian)",
    "Language A - Language and Literature (Urdu)",
    "Language A - Language and Literature (Vietnamese)",
    "Language A - Language and Literature (Welsh)",
    "Literature and Performance",
    
    # Group 2: Language Acquisition
   "Language B (Arabic)",
    "Language B (Chinese)",
    "Language B (Danish)",
    "Language B (Dutch)",
    "Language B (English)",
    "Language B (Finnish)",
    "Language B (French)",
    "Language B (German)",
    "Language B (Hebrew)",
    "Language B (Indonesian)",
    "Language B (Italian)",
    "Language B (Japanese)",
    "Language B (Korean)",
    "Language B (Norwegian)",
    "Language B (Portuguese)",
    "Language B (Russian)",
    "Language B (Spanish)",
    "Language B (Swedish)",
    "Language B (Turkish)",
    "Language ab initio (Arabic)",
    "Language ab initio (Bengali)",
    "Language ab initio (Chinese)",
    "Language ab initio (Dutch)",
    "Language ab initio (French)",
    "Language ab initio (German)",
    "Language ab initio (Gujarati)",
    "Language ab initio (Hindi)",
    "Language ab initio (Italian)",
    "Language ab initio (Japanese)",
    "Language ab initio (Korean)",
    "Language ab initio (Malay)",
    "Language ab initio (Portuguese)",
    "Language ab initio (Russian)",
    "Language ab initio (Spanish)",
    "Language ab initio (Swahili)",
    "Language ab initio (Tamil)",
    "Language ab initio (Urdu)",
    "Classical Languages (Latin)",
    "Classical Languages (Classical Greek)",
    "Classical Languages (Latin, Classical Greek)",
    
    # Group 3: Individuals and Societies
    "Business Management",
    "Economics",
    "Geography",
    "Global Politics",
    "History",
    "Information Technology in a Global Society (ITGS)",
    "Philosophy",
    "Psychology",
    "Social and Cultural Anthropology",
    "World Religions",
    
    # Group 4: Sciences
    "Biology",
    "Chemistry",
    "Computer Science",
    "Design Technology",
    "Environmental Systems and Societies",
    "Physics",
    "Sports, Exercise and Health Science",
    
    # Group 5: Mathematics
    "Mathematics - Analysis and Approaches",
    "Mathematics - Applications and Interpretation",
    
    # Group 6: The Arts
    "Dance",
    "Film",
    "Music",
    "Theatre",
    "Visual Arts",

    "Extended Essay (EE)",
    "Theory of Knowledge (TOK)",
    "Creativity, Activity, Service (CAS)"
])
if courses_that_user_take:
    higher_levels = st.multiselect("Choose HL Subjects", courses_that_user_take)

for subjects in courses_that_user_take.copy():
    if subjects in higher_levels:
        courses_that_user_take.remove(subjects)
        courses_that_user_take.append(f"{subjects} HL")
    else:
        courses_that_user_take.remove(subjects)
        courses_that_user_take.append(f"{subjects} SL")
list_of_teachers = []
for course in courses_that_user_take:
    list_of_teachers.append(st.text_input(f"Who is your teacher for {course}?"))

subject_with_teacher = list(zip(courses_that_user_take, list_of_teachers))

if st.button("Save"):
    dict_to_dump = {
        "Student" : user,
        "Subject" :subject_with_teacher,
        "ID" : student_ID
    }

    file_path = 'user_profiles.json'

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the existing data
        with open(file_path, 'r') as infile:
            try:
                existing_data = json.load(infile)
                # Ensure it's a list
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append the new data
    existing_data.append(dict_to_dump)

    # Write the updated list back to the file with indentation
    with open(file_path, 'w') as outfile:
        json.dump(existing_data, outfile, indent=4)
    st.write("Saved successfully!")

    st.page_link("Homepage.py", label="Go back to the Homepage", icon = "🏠")

