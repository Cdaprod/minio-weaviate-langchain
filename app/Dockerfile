FROM python:3.9-slim
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt --verbose
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
