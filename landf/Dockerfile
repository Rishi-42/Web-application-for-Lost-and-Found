FROM python:3.8-slim-buster
WORKDIR /lostandfound

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt && echo "Requirements installed successfully"
COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
