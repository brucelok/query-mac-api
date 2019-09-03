FROM python:2.7-slim

WORKDIR /app
COPY . /app

# Run macapi.py when the container launches
ENTRYPOINT ["python", "macapi.py"]

# parse args from docker run
CMD []
