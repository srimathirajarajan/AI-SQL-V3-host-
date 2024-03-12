import os
from pathlib import Path
from app_secrets import OPENAI_API_KEY
from sql_execution import execute_mysql_query
import streamlit as st
from PIL import Image
from langchain import OpenAI, LLMChain
from langchain.prompts import load_prompt

# Setup env variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# Project root directory
#root_path = [p for p in Path(__file__).parents if p.parts[-1] == "AI SQL - V3"][0]

# Frontend
st.title("AI SQL Assistant")
user_input = st.text_input("Enter your query")
tab_titles = ["Result", "Query"]
tabs = st.tabs(tab_titles)


# Create the prompt
prompt_template = load_prompt('tpch_prompt.yaml')
llm = OpenAI(temperature=0)
sql_generation_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

if user_input:
    sql_query = sql_generation_chain(user_input)
    if 'text' in sql_query:
        generated_sql = sql_query['text']
        with tabs[1]:
            st.write("Generated SQL Query:")
            st.code(generated_sql)

        try:
            if st.button("Execute Query"):
                result = execute_mysql_query(generated_sql)
                if result is not None:
                    with tabs[0]:
                        st.write("Query Execution Result:")
                        st.write(result)  # Display the query execution result
                else:
                    with tabs[0]:
                        st.write("No result returned from the database.")
        except Exception as e:
            st.write(f"Error executing SQL query: {e}")
    else:
        st.write("Error generating SQL query. Please check your input and try again.")
