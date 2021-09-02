FROM python:3.9.7

RUN mkdir /service
COPY access/ /service/access/
WORKDIR /service/access/view

RUN python -m pip install -U pip
RUN python -m pip install django

EXPOSE 8000
ENV PYTHONPATH=.
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
