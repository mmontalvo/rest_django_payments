FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /rest_django_payments
WORKDIR /rest_django_payments
COPY requirements.txt /rest_django_payments/
RUN pip install -r requirements.txt
ADD . /rest_django_payments/

CMD python rest_django_payments/manage.py runserver 0.0.0.0:8200
