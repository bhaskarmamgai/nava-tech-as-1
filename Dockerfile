FROM python:3.10-slim

WORKDIR /code

COPY requirement.txt requirement.txt

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

COPY .env .env

EXPOSE 8000
CMD ["uvicorn", "organizations.main:app", "--host", "0.0.0.0", "--port", "8000"]
