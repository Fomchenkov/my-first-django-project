FROM python:3

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENV NAME app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
