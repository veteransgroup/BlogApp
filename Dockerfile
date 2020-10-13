FROM python:3
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/veteransgroup/BlogApp.git && pip3 install -r BlogApp/requirements.txt
WORKDIR /BlogApp
RUN python manage.py collectstatic
COPY ./uwsgi.ini /BlogApp

