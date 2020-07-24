FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /manning/rest_django_payments
WORKDIR /manning/rest_django_payments
COPY requirements.txt /manning/rest_django_payments/
RUN pip install -r requirements.txt
RUN pip install -r mysqlclient
ADD . /manning/rest_django_payments/

EXPOSE 8080

CMD ["gunicorn", "--bind", ":8080", "rest_django_payments.wsgi:application"]
