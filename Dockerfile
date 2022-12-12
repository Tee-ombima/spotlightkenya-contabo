#choose os
FROM python:3.10

LABEL maintainer="www@spotlightkenya.club"
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

#create wd on the container
WORKDIR /app/

#copy file to container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#copy all other folders to the container too
COPY . .


#run command in the terminal of the container. port ensures app is available from main comp

#create .dockerignore. to prevent copying of env
