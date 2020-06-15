FROM node
FROM python:3.6-slim-stretch

ENV PYTHONUNBUFFERED 1
# Set the working directory.
WORKDIR /

# Copy the file from your host to your current location.
COPY . .
# COPY package.json .
# COPY requirements.txt .
# Run the command inside your image filesystem.
# RUN pip install pipenv
# RUN pipenv shell
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs

RUN pip install -r requirements.txt
RUN npm install

RUN python ./leadmanager/manage.py makemigrations
RUN python ./leadmanager/manage.py migrate
RUN npm run build



# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8000

# Run the specified command within the container.

CMD ["python", "leadmanager/manage.py", "runserver", "0.0.0.0:8000"]

# Copy the rest of your app's source code from your host to your image filesystem.
# COPY . .