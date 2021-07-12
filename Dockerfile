FROM golang:1.16-alpine

# Set the Current Working Directory inside the container
WORKDIR /app

# We want to populate the module cache based on the go.{mod,sum} files.
COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN echo ls

# This container exposes port 8080 to the outside world
EXPOSE 3000

# Build
CMD [ "cd server/" ]
