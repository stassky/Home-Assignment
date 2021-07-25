FROM python:3
ADD test.py /
RUN pip install flask
CMD [ "python3", "./test.py" ]