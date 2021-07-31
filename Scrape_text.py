import requests
import html5lib
import bs4

from bs4 import BeautifulSoup
def interview_texts():

  URL = "https://www.guru99.com/machine-learning-interview-questions.html"
  r = requests.get(URL)
    
  soup = BeautifulSoup(r.content, 'html5lib')

  question = []
  for i in soup.find_all('strong'):
    question.append(i.text+ " ")
  question = question[:-1]


  context = []
  for a in soup.find_all('p'):
    if a.text not in question:
      context.append(a.text)
  context = context[1:]
  return context
