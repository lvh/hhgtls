FROM debian:testing
RUN apt-get update
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN curl -sL https://asciinema.org/install | sh # curl | sh for SECURITY
RUN pip install twisted[tls] treq requests
