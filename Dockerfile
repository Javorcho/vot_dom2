FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir psycopg2-binary

CMD ["python", "quiz_game.py"]
