FROM python:3.11-alpine

LABEL maintainer="Ethan Nguyen"

COPY . /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

RUN pip install -r requirements.txt

CMD ["python", "-u", "consumer.py"]