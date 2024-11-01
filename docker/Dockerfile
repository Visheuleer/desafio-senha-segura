FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r config/requirements.txt


EXPOSE 8080

CMD ["python", "src/__main__.py"]