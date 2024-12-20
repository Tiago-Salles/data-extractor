FROM python:3.13-slim

RUN apt-get update -y && apt-get install -y \
    build-essential \
    gcc \
    pkg-config \
    default-libmysqlclient-dev

WORKDIR app

COPY app /app

CMD ["tail", "-f", "/dev/null"]