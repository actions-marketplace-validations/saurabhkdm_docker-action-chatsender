FROM python:3.6

# Create app directory
WORKDIR .

# Install app dependencies
COPY . .

RUN pip install -r requirements.txt

CMD [ "/entrypoint.sh" ]
