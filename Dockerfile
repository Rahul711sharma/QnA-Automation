FROM python:3.9

RUN pip install -r requiremts.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
