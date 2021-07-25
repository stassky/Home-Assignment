FROM python:3

RUN pip install flask

COPY test.py /

CMD [ "python", "./test.py" ]