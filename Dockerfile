FROM python:3.7.11-alpine
# RUN apk --update add bash nano
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
# COPY ./home_task
WORKDIR /home_task
ADD . /home_task
# COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
CMD ["python","app.py"]