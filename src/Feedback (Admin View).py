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

if not st.session_state.authentication_status:
    st.info('Please Login from the Home page and try again.')
    st.stop()

st.header("Welcome to the Feedback Page")

user = st.session_state["STUDENT_NAME"]
# genre = st.selectbox("Select the subject that you need help with",[item[0] for item in st.session_state["STUDENT_SUBJECT"]])
# for elem in st.session_state["STUDENT_SUBJECT"]:
#     if elem[0] == genre:
#         teacher = elem[1]
file_path = 'tutor_log.json'

if os.path.exists(file_path):
    # Read the existing data
    with open(file_path, 'r') as infile:
        try:
            existing_data = json.load(infile)
            # Ensure it's a list
        except json.JSONDecodeError:
            st.error("Error reading JSON file.")

client = OpenAI(api_key=get_key())

assistant_to_analyze = client.beta.assistants.create(
    name="Academic Counselor for IB subjects",
    instructions=
    f"""You are an expert IB academic counselor/analyst. Read the json input and Use your knowledge base to give constructive feedback to student.
    First, categorize each student and their questions by topic on each IB subject, the topic may include an assessment type (e.g., Paper 1, Paper 2, IA, EE, etc.). 
    Second, using the category, evaluate the conversation log to identify weaknesses and strengths in each category. 
    Keep list of topics to maximum 6.
    Return the response in the following JSON format:
    [
        {{
            "student_name": "user1",
            "subject": "math",
            "feedback": {{
                "topics": {{
                    "topic1": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }},
                    "topic2": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }}
                }}
            }},
            "teacher": "teacher1"
        }},
        {{
            "student_name": "user1",
            "subject": "English A",
            "feedback": {{
                "topics": {{
                    "topic1": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }},
                    "topic2": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }}
                }}
            }},
            "teacher": "teacher1"
        }}
    ]""",
    model="gpt-4o",
    tools=[{"type": "file_search"}],
)

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"{existing_data}"
)
log_global = None
# Run if question is entered
with st.spinner('Creating Feedback'):
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_to_analyze.id,
        instructions=f"""You are an expert IB academic counselor/analyst. Read the json input and Use your knowledge base to give constructive feedback to student.
    First, categorize each student and their questions by topic on each IB subject, the topic may include an assessment type (e.g., Paper 1, Paper 2, IA, EE, etc.). 
    Second, using the category, evaluate the conversation log to identify weaknesses and strengths in each category. 
    Keep list of topics to maximum 6.
    Return the response in the following JSON format:
    [
        {{
            "student_name": "user1",
            "subject": "math",
            "feedback": {{
                "topics": {{
                    "topic1": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }},
                    "topic2": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }}
                }}
            }},
            "teacher": "teacher1"
        }},
        {{
            "student_name": "user1",
            "subject": "English A",
            "feedback": {{
                "topics": {{
                    "topic1": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }},
                    "topic2": {{
                        "strengths": "...",
                        "weaknesses": "..."
                    }}
                }}
            }},
            "teacher": "teacher1"
        }}
    ]""",
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        # Need to understand how this code works
        for m in messages:
            if m.role != "user":
                st.markdown(m.content[0].text.value)

    else:
        st.markdown(run.status)
