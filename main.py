from unstructured.partition.pdf import partition_pdf
import streamlit as st
import os

def use_unstructured(file_content, file_name):
    with open(file_name, "wb") as f:
        f.write(file_content)
    elements = partition_pdf(file_name)  
    os.remove(file_name)
    return "\n\n".join([str(el) for el in elements])
uploaded_files = st.file_uploader("*Choose PDF files*", type=["pdf", "csv", "xlsx", "docx", "pptx"], accept_multiple_files=True)

for uploaded_file in uploaded_files:
    file_content = uploaded_file.read()
    temp_file_name = uploaded_file.name
    parsed_text = use_unstructured(file_content, temp_file_name)
st.write(parsed_text)