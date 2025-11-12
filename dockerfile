FROM python:3.11-slim

WORKDIR /app/

COPY requirements.txt . app/
COPY weather_app/ /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["streamlit", "run", "main.py", "--server.port=5000", "--server.address=0.0.0.0"]