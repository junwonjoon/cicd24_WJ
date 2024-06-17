"""
Welcome to the main page
Author: Wonjoon Jun
Date: Jun 7, 2024
Please view README.md for more information.
"""
import streamlit as st
import pandas as pd
from typing_extensions import override
import json
import os

def get_key()->str:
    try:
        with open("key.txt", 'r') as infile:
            return infile.read()
    except OSError:
        st.error("failed to retrieve API KEY")
        return ""

st.set_page_config(
    page_title="TAILOR MVP",
    page_icon="✏️",
    initial_sidebar_state = "collapsed",
)

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


password = "1234"
st.title("TAILOR")
status = st.selectbox("Choose your status:", ["Faculty", "Student"])

if status == "Faculty":
    password_input = st.text_input("Enter admin password:")
    if st.button("Continue"):
        if password_input == password:
            st.page_link("pages/Feedback (Admin View).py", label="View Feedback for All Students", icon = "🧑‍🎓")
            st.session_state.authentication_status = True 
        else:
            st.error("Incorrect Password")
else:
    st.page_link("pages/Create New Student.py", label="I am a new student")
    file_path_for_user_profile = 'user_profiles.json'
    if os.path.exists(file_path_for_user_profile):
        # Read the existing data
        with open(file_path_for_user_profile, 'r') as infile:
            try:
                existing_data = json.load(infile)
                # Ensure it's a list
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    if existing_data:
        # st.write(existing_data)
        names = [items["Student"] for items in existing_data]
        IDs = [items["ID"] for items in existing_data]
        profile = zip(names, IDs)
        STUDENT_PROFILE = st.radio("Choose your profile (This too later should be automatic)", profile)
        if st.button("The student above is me"):
            st.session_state["STUDENT_NAME"] = STUDENT_PROFILE[0]
            st.session_state["STUDENT_ID"] = STUDENT_PROFILE[1]
            for profiles in existing_data:
                if profiles["Student"] == st.session_state["STUDENT_NAME"] and profiles["ID"] ==  st.session_state["STUDENT_ID"]:
                    st.session_state["STUDENT_SUBJECT"] = list(profiles["Subject"])
                    st.page_link("pages/My Tutor.py", label="My tutor", icon = "🧑🏽‍🏫")
                    st.page_link("pages/Feedback (Student View).py", label="Feedback Page", icon = "📈")

        

    # if st.button("Continue"):
    #     #change the list later
    #     if unique_code != "" and unique_code in [unique_code]:
    #         st.page_link("pages/Feedback (Student View).py", label="View Feedback", icon = "🧑‍🎓")
    #         st.page_link("pages/My Tutor.py", label="My tutor", icon = "🧑‍🏫")
    #     else:
    #         st.error("Incorrect Code")
