FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt



