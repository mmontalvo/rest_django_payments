FROM python:3.7.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /manning/rest_django_payments
WORKDIR /manning/rest_django_payments
COPY requirements.txt /manning/rest_django_payments/
RUN pip install -r requirements.txt
ADD . /manning/rest_django_payments/

EXPOSE 8200

CMD ["gunicorn", "--chdir", "rest_django_payments", "--bind", ":8200", "rest_django_payments.wsgi:application"]
