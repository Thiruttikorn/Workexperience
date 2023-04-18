FROM python:3.8
WORKDIR /DjangoAPI

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install attrs cryptography

EXPOSE 7000

CMD ["gunicorn", "DjangoAPI.wsgi", "-b", ":7000"]
