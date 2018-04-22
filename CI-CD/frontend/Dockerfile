FROM ubuntu:latest
MAINTAINER miki
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libmysqlclient-dev 
COPY src/* /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 9001
ENTRYPOINT ["python"]
CMD ["app.py"]
