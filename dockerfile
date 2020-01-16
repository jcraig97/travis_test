FROM python:3
RUN mkdir /code/
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY script.py /code/
RUN ["python","/code/script.py"]
