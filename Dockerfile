FROM node:12
FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /

COPY . .

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm

RUN pip install -r requirements.txt
RUN npm install

RUN python ./leadmanager/manage.py makemigrations
RUN python ./leadmanager/manage.py migrate
RUN npm run build

EXPOSE 8000

CMD ["python", "leadmanager/manage.py", "runserver", "0.0.0.0:8000"]