FROM python:3.11-alpine

COPY . /app

WORKDIR /app

# RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["python", "-u", "main.py"]