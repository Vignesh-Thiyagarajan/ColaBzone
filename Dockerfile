# Use an Alpine-based Python image
FROM python:3.11-alpine3.18

LABEL maintainer="https://github.com/Vignesh-Thiyagarajan"

ENV PYTHONUNBUFFERED 1

# Install required system packages
RUN apk update && \
    apk add --no-cache mysql-dev gcc musl-dev

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt files to the container
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY . .

ARG DEV=false

# Install Python packages and clean up
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; then pip install --no-cache-dir -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp

# Add a non-root user (optional)
RUN adduser --disabled-password --no-create-home colabzone_user

# Set the user for subsequent commands (optional)
USER colabzone_user

