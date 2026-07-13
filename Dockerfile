FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y procps

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
