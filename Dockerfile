FROM python:3.9-slim-buster as base
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM base as app 
WORKDIR /app
COPY ./src .
CMD [ "python3", "server.py"]

FROM base as test
WORKDIR /app
COPY . .
CMD ["python", "-m", "pytest"]

