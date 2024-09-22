import streamlit as st
from summarization import generate_abstractive_summary  # Use the function from your summarization code

# Streamlit web app
st.title("Text Summarization App")
input_text = st.text_area("Enter the text you want to summarize", height=150)

if st.button("Generate Summary"):
    if input_text.strip():
        summary = generate_abstractive_summary(input_text)  # Directly generate the summary without preprocessing
        
        st.subheader("Generated Summary:")
        st.write(summary)  # Display the summary directly
    else:
        st.error("Please enter some text to summarize.")
