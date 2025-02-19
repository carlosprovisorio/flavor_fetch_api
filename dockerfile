FROM python:3.9-alpine3.13
LABEL maintainer="github.com/carlosprovisorio"

# Prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Copy the requirements.txt file into the container
COPY ./requirements.txt /tmp/requirements.txt

COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts

# Copy the app directory into the container
COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Expose port 8000 to allow traffic
EXPOSE 8000

ARG DEV=false

# Create a Python virtual environment and install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts


# Set the path to include the virtual environment
ENV PATH="/scripts:/py/bin:$PATH"

# Switch to the django-user for running the application
USER django-user

CMD ["run.sh"]