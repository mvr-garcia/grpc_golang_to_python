# Country Infopédia

This is a server-client application where the server performs a search on a public API and retrieves the country information searched on the client. Communication between server and client is done using gRPC.

#### To know:

This was my first contact with gRPC, a technology that should be the main communication technology between systems contained in microservices architecture.

Credits for the idea and teachings to [Anderson Borges](https://medium.com/@andersonborges_70700).

## Requirements

To make the magic happen, you just need to have installed:

* Docker

## Starting the application

```bash
make grpc-up
```

## To use de application without Docker

I recommend use Docker. But if you want run without it,
you need to have installed:

- Go 1.16
- Python 3.9.5

```bash
git clone [link]
```
To start the server:

```bash
go get .
```
```bash
go run start.go
```

To start the client:

First: Change the value of th ```host``` variable in client/app.py to "localhost".
"server" is the address to find the server in container.

```bash
cd client/
```
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 -m flask run
```

Access the service in [http://localhost:5000](http://localhost:5000/).

## Special thanks

To the [Matheus Rocha](https://github.com/matheusrocha-mb)
Your help with the Docker in golang was essential.

## Authors

Marcos Garcia   
e-mail: mvrgarcia05@gmail.com
