FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["bash","/app/entrypoint.sh"]
