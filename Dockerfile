FROM python:3

RUN mkdir /app
WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "manage.py", "runserver"]
