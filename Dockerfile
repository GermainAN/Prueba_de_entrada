FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn asyncpg databases

EXPOSE 8000