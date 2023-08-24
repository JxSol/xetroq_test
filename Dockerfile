FROM python:3.11
LABEL authors="JxSol"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Обновляем систему
RUN apt update && \
    apt install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py makemigrations --noinput \
    && python manage.py migrate --noinput \
    && python manage.py loadtestdata \
    && python manage.py spectacular --color --file schema.yml \
    && gunicorn qortex.wsgi:application --bind 0.0.0.0:8000