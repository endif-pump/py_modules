FROM python:3.10.11-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN addgroup -S testgroup && adduser -S testuser -G testgroup -u 1000

USER testuser

CMD ["pytest", "--verbose"]

