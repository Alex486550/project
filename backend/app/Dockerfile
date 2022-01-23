

#FROM python:3
#RUN mkdir /app
#WORKDIR /app
#COPY . /app/
#RUN pip3 install --upgrade pip
#RUN pip3 install -r requirements.txt
#EXPOSE 80
#CMD ['python3', 'backend.py']


FROM python:3
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y nano && apt-get install -y iputils-ping
EXPOSE 8081
#CMD ["python3", "backend.py", "--host=0.0.0.0", "--port=8080"]
CMD ["ping", "ya.ru"]

