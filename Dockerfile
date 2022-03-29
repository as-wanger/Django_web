FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /Django_web
WORKDIR Django_web
COPY . /Django_web/
RUN pip install -r requirements.txt

RUN mkdir -p /Django_web/mysqld && chmod -R 777 /Django_web/mysqld

EXPOSE 8000