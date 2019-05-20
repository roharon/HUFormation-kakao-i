FROM ubuntu:18.04

MAINTAINER roharon98@gmail.com
RUN apt-get install python3 python3-pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]