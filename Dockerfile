FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /lotr_api
WORKDIR /lotr_api
COPY requirements.txt /lotr_api/
RUN pip install -r requirements.txt
COPY . /lotr_api/
