FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "messagesender.py" ]
