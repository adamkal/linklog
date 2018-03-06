FROM python:3.6-jessie

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install
ENV FLASK_APP=linklog.py

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]
EXPOSE 5000