FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/main.py .

CMD ["python", "main.py"] 