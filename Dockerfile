FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY . .

RUN uv pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]