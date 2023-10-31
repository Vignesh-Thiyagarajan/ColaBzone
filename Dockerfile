# Use an Alpine-based Python image
FROM python:3.11-alpine3.18

# Update pip during image build
RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DEV=false

# Install required system packages
RUN apk update && \
    apk add --no-cache mysql-dev gcc musl-dev

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt files to the container
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY . .

# Install Python packages and clean up
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then pip install --no-cache-dir -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp

# Add a non-root user (optional)
RUN adduser --disabled-password --no-create-home colabzone_user

# Set the user for subsequent commands (optional)
USER colabzone_user
