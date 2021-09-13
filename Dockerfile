FROM python:3.9-slim-bullseye

RUN pip install poetry
COPY . /run

RUN cd /run && \
    poetry export -f requirements.txt --output requirements.txt && \
    pip install -r requirements.txt

ENTRYPOINT ["/run/entrypoint.sh"]