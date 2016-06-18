FROM mhart/alpine-node:latest
RUN npm install -g http-server
ADD . /code
WORKDIR /code/tester
EXPOSE 4000
CMD ["http-server", "-p", "4000"]