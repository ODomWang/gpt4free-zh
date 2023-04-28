import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
import you

def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        result = you.Completion.create(
            prompt = question)
        
        return result['response']
    
    except Exception as e:
        # Return error message if an exception occurs
        return f'报错信息: {e}'


# Set page configuration and add header
st.set_page_config(
    page_title="GPT4free",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
             
        'About': "### gptfree GUI"
    }
)
st.header('GPT4free')

# Add text area for user input and button to get answer
question_text_area = st.text_area(
    '🤖 问任何问题:', placeholder='Explain quantum computing in 50 words')
if st.button('🧠 发送',key=13):
    cnstr='使用中文回复：'
    question_text_area+=cnstr
    answer = get_answer(question_text_area)
    # Display answer
    
    utf8_decode = answer.encode().decode("unicode_escape").replace('”}','').replace('"}','')
    st.caption("回复 :")
    st.markdown(utf8_decode)

# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
