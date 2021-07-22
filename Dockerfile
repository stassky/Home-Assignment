FROM python:3
ADD api.py /
CMD [ "python3", "./api.py" ]