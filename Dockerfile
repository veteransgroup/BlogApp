FROM python:3
ENV PYTHONUNBUFFERED 1
COPY . /BlogApp
RUN pip3 install -r BlogApp/requirements.txt
WORKDIR /BlogApp
RUN python manage.py collectstatic
