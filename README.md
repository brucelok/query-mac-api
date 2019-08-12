# Query Mac API
The project demonstrates the simple API in Python to query Mac address from https://macaddress.io, and return the vendor name associated with Mac address.

The python script accepts 2 arguments:
1. your API key from macaddress.io
2. the target mac address you lookup

## Prerequisites
* Python >= 2.7
* Docker >= 19.0

## Clone the project to local
```
$ git clone https://gitlab.com/lok.bruce/query-mac-api.git
```

## Two ways to run the program:

### 1. Standard CLI
your can directly it from your Linux terminal
```
$ python macapi.py your_api_key a4:83:e7:7a:0b:8c
Apple, Inc
```

### 2. Run from Docker container
1. first build the light Python image from the Dockerfile
```
$ docker build -t apitest .
```

2. Docker run now
```
$ docker run --rm apitest your_api_key a4:83:e7:8b:0c:9b
Apple, Inc
```
