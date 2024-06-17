"""
This is page 1
Author: Wonjoon Jun
Date: Jun 7, 2024
Please view README.md for more information.
"""
from Homepage import get_key
import streamlit as st
from openai import OpenAI, AssistantEventHandler
from datetime import datetime
import json
import os


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

st.header(f"{st.session_state["STUDENT_NAME"] if st.session_state["STUDENT_NAME"] is not None else "Student"}'s Tutor")
st.caption("Beta Version")
st.page_link("Homepage.py", label="Homepage", icon = "🏠")
st.page_link("pages/Feedback (Student View).py", label="Feedback Page", icon = "📈")

#This needs to be actual log later on + Change this to OOP

user = st.session_state["STUDENT_NAME"] 
genre = st.selectbox("Select the subject that you need help with",[item[0] for item in st.session_state["STUDENT_SUBJECT"]])
for elem in st.session_state["STUDENT_SUBJECT"]:
    if elem[0] == genre:
        teacher = elem[1]
question = st.chat_input(f"What is your question regarding \'{genre}\'")
file_path = 'tutor_log.json'

if os.path.exists(file_path):
    # Read the existing data
    with open(file_path, 'r') as infile:
        try:
            existing_data = json.load(infile)
            # Ensure it's a list
        except:
            pass

list_of_questions_asked_for_this_subject = []
list_of_answers_for_this_subject = []
if existing_data:
    for entry in existing_data:
        student_name = entry['Student'][0]
        subject = entry['Subject']
        if student_name == user and subject == genre:
            with st.chat_message("user"):
                past_question = entry['Question']
                list_of_questions_asked_for_this_subject.append(past_question)
                st.write(past_question)
            with st.chat_message("assistant"):
                past_response = entry['Answer']
                list_of_answers_for_this_subject.append(past_response)
                st.write(past_response)


if question is not None:
    with st.chat_message("user"):
            st.write(question)

#From ChatGPT Website
client = OpenAI(api_key=get_key())

prompt_for_assistant = f"""You are a personal IB {genre} tutor. 
Be friendly, if your a language tutor speak in that language.
Be professional, and polite, keep it PG. 
Provide examples of assist you can give when first meeting, you can guide them, but never giveout answers in answer sheet(if answer sheet is given in file search).
Never complete whole work for them.
Also, after each explanation ask the user if they understood.
"""
prompt_for_question_instruction = f""" Please address the user as {user.split()[0]}. 
The user has a premium account. 
You are a personal IB DP {genre} tutor. 
Write and run code to answer {genre} questions, if given .
The past conversation with the student were the following: {list(zip(list_of_questions_asked_for_this_subject[-30:],list_of_answers_for_this_subject[-30:]))}, create a helpful and detailed response based on your knowledge and past conversation
"""

assistant_for_student = client.beta.assistants.create(
  name=f"{genre} Tutor",
  instructions=prompt_for_assistant,
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content=f"{question}"
)
log_global = None
#Run if question is entered
if question is not None:
    with st.spinner('Loading response'):
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant_for_student.id,
            instructions=prompt_for_question_instruction,
        )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
        #Need to understand how this code works
        for m in messages:
            if m.role != "user":
                with st.chat_message(f"{m.role}"):
                    try:
                        gpt_response = m.content[0].text.value
                        st.write(gpt_response)
                    except:
                        st.write("Error occured while creating the response")

    else:
        st.markdown(run.status)


    dict_to_dump = {
        "Time" : datetime.utcnow().isoformat(),
        "Student" : (user, st.session_state["STUDENT_ID"]),
        "Subject" : genre,
        "Teacher" : teacher,
        "Question" : question,
        "Answer" :gpt_response
    }


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
