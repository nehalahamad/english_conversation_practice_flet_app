FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY Dockerfile ./Dockerfile
COPY fly.toml ./fly.toml

EXPOSE 8000

CMD ["python", "src/main.py"]