FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /rest_django_payments
WORKDIR /rest_django_payments
COPY requirements.txt /rest_django_payments/
RUN pip install -r requirements.txt
ADD . /rest_django_payments/

EXPOSE 8080

CMD ["gunicorn", "--chdir", "rest_django_payments", "--bind", ":8080", "rest_django_payments.wsgi:application"]
