import Scrape_text
import streamlit as st
import Clean
import transformers
from transformers import pipeline
from transformers.pipelines import base
import requests
import html5lib
import bs4
from bs4 import BeautifulSoup


context = Clean.clean_interview(Scrape_text.interview_texts()[0:1])

nlp = pipeline("question-answering")


try:
    # Project Title
    st.header("Welcome to Automated Q&A bot")


    # To fetch the query that is the question  
    question=st.text_input('Ask a question here:') 


    answer = nlp(question=question, context=context)
    st.text(answer['answer'])

except:
    print("Please Type a Question")


