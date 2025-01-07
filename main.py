import os
import streamlit as st
from dotenv import load_dotenv
from few_shot import FewShotPosts
from langchain_groq import ChatGroq
from post_generator import generate_post

## Loading environment
load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192")

## Posts length and language types 
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.subheader("LinkedIn Post Generator: Testing")
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)

if __name__ == "__main__":
    main()
