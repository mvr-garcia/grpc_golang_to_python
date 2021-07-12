FROM golang:1.16-alpine

RUN mkdir /app
## We copy everything in the root directory
## into our /app directory
ADD . /app

## We specify that we now wish to execute 
## any further commands inside our /app
## directory
# Set the Current Working Directory inside the container
WORKDIR /app

RUN go build -o main .

# This container exposes port to the outside world
EXPOSE 3000

# Build
CMD [ "/app/main" ]
