#FROM python:3.7
#RUN mkdir /app
#WORKDIR /app
#COPY . /app/
#RUN pip3 install -r requirements.txt
#EXPOSE 80
#CMD ["python3", "/app/front.py"]

FROM python:3
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y nano
EXPOSE 80
#COPY . .
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]

#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
