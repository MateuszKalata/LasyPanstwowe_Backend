FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 5000
CMD ["gunicorn", "--workers=3", "-b", "0.0.0.0:5000", "app:app"]