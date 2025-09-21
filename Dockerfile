# Dockerfile

FROM python:3.10-slim
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 👇 This fixes the ModuleNotFoundError
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["python", "src/main.py"]
