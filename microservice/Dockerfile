FROM python:3.7.6-stretch

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ARG PORT
ENV PORT $PORT
ENV HOST 0.0.0.0

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["app.py"]