FROM python:3.6.7
RUN pip install numpy
RUN pip install tensorflow
RUN pip install Django==2.1.4
COPY . /home
WORKDIR /home
RUN python manage.py migrate
EXPOSE 8000