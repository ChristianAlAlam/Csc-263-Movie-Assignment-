
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies including Pillow requirements
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    pkgconfig \
    jpeg-dev \
    zlib-dev \
    libjpeg

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Create static directory if it doesn't exist
RUN mkdir -p /app/static

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]