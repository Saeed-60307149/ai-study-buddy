FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY . .

EXPOSE 5000
EXPOSE 8000
EXPOSE 27017

CMD ["python", "app.py"]