"""
This is a Feedback page 
Author: Wonjoon Jun
Date: Jun 7, 2024
Please view README.md for more information.
"""
import streamlit as st
import pandas as pd
from openai import OpenAI
import os
import json
from Homepage import get_key

st.set_page_config(
    page_title="TAILOR MVP",
    page_icon="✏️",
    initial_sidebar_state="collapsed",
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

user = st.session_state["STUDENT_NAME"]
st.header(f"Feedback Page for {user}")
st.page_link("Homepage.py", label="Homepage", icon="🏠")
st.page_link("pages/My Tutor.py", label="My tutor", icon="🧑🏽‍🏫")
genre = st.selectbox("Select the subject that you want to hear feedback",
                     [item[0] for item in st.session_state["STUDENT_SUBJECT"]])
for elem in st.session_state["STUDENT_SUBJECT"]:
    if elem[0] == genre:
        teacher = elem[1]
file_path = 'tutor_log.json'

if os.path.exists(file_path):
    # Read the existing data
    with open(file_path, 'r') as infile:
        try:
            existing_data = json.load(infile)
            # Ensure it's a list
        except json.JSONDecodeError:
            st.error("Error reading JSON file.")
list_of_questions_asked_for_this_subject = []
list_of_answers_for_this_subject = []
if existing_data:
    for entry in existing_data:
        student_name = entry['Student'][0]
        subject = entry['Subject']
        if student_name == user and subject == genre:
            past_question = entry['Question']
            list_of_questions_asked_for_this_subject.append(past_question)
            past_response = entry['Answer']
            list_of_answers_for_this_subject.append(past_response)

dict_to_analyze = {}
for i in range(len(list_of_questions_asked_for_this_subject)):
    dict_to_analyze[list_of_questions_asked_for_this_subject[i]] = list_of_answers_for_this_subject[i]

system_prompt = f"""You are an expert IB academic counselor/analyst. Read the python dictionary input and Use your knowledge base to give constructive feedback to student.
    First, categorize each student and their questions by topic on each IB subject, the topic may include an assessment type (e.g., Paper 1, Paper 2, IA, EE, etc.). 
    Second, using the category, evaluate the conversation log to identify student's weaknesses and strengths in each category. 
    Keep list of topics to maximum 6.
    Return the response in the following JSON format:
    [
        {{
            "identifed_topic": {{
                "strengths": "...",
                "weaknesses": "..."
            }},
            "...": {{
                "strengths": "...",
                "weaknesses": "..."
            }}
        }}
    ]"""

client = OpenAI(api_key=get_key())
with st.spinner('Creating Feedback'):
    chat_completion = client.chat.completions.create(
        model="gpt-4-turbo",
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": str(dict_to_analyze)}
                  ])
    data = chat_completion.choices[0].message.content
feedback = json.loads(data)
with open(f"{user} Feedback({genre}).json", 'w') as outfile:
    json.dump(feedback, outfile, indent=4)

try:
    for topic, details in feedback.items():
        strengths = details['strengths']
        weaknesses = details['weaknesses']
        st.header(f"Topic: {topic}")
        st.subheader(f"Strengths")
        st.write(strengths)
        st.subheader(f"Weaknesses")
        st.write(weaknesses)
except:
    st.write(feedback)

# *******THIS CODE IS TO BE LATER USED FOR FILE SEARCH FEATURE, THE CODE IS TEMPORARILY DISABLED DUE TO INCONSISTENCY IN PRINTING JSON FILES***
# assistant_to_analyze = client.beta.assistants.create(
#   name="Academic Counselor for IB subjects",
#   instructions= system_prompt,
#   model="gpt-4o",
#   tools=[{"type": "file_search"}],
# )


# thread = client.beta.threads.create()
# message = client.beta.threads.messages.create(
#   thread_id=thread.id,
#   role="user",
#   content=f"{dict_to_analyze}"
# )
# log_global = None
# #Run if question is entered
# with st.spinner('Creating Feedback'):
#     run = client.beta.threads.runs.create_and_poll(
#         thread_id=thread.id,
#         assistant_id=assistant_to_analyze.id,
#         instructions = system_prompt,
#     )

#     if run.status == 'completed': 
#         messages = client.beta.threads.messages.list(
#         thread_id=thread.id
#     )
#         for m in messages:
#             if m.role != "user":
#                 json_response_raw = m.content[0].text.value  
#     else:
#         st.markdown(run.status)


# view feedback for Student name
