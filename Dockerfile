FROM python:3
ADD api-3.py /
CMD [ "python3", "./api-3.py" ]