FROM python:3.5-alpine
RUN apk add --no-cache git make perl
ADD ./api/requirements.txt /code/api/
RUN pip install --upgrade pip
RUN pip install -r /code/api/requirements.txt
ADD . /code
WORKDIR /code/api
EXPOSE 5000
CMD ["python", "-u", "/code/api/app.py"]