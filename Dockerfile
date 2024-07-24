FROM python:3.12-slim

WORKDIR /app

ADD requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]