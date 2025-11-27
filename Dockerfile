FROM python:3.11 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /base

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# створюємо папку для медіа
RUN mkdir -p /media

FROM base as dev
CMD python manage.py runserver 0.0.0.0:8000

FROM base as prod
COPY . .
CMD gunicorn base.wsgi:application --bind 0.0.0.0:$PORT


