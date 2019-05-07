FROM ubuntu:18.04

MAINTAINER roharon98@gmail.com
RUN echo 'apt-get update'
RUN apt-get update && apt-get install -y apt-transport-https
RUN echo 'install python3 python3-pip'
RUN apt-get install -y python3 python3-pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]