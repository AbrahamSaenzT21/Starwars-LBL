FROM python:3.11.2-alpine

WORKDIR /app

ENV PORT=3000

COPY requirements.txt .

COPY logic_file.py .

COPY data_access.py .

RUN pip install -r requirements.txt

EXPOSE 3000

COPY app.py .

CMD ["python", "/app/app.py"]