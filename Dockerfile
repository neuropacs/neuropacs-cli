# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container
# WORKDIR /usr/src/app

# Copy the current directory contents into the container
# COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt


# Define build-time variables for server_url and api_key
ARG server_url
ARG api_key

# Set the environment variables
ENV SERVER_URL=$server_url
ENV API_KEY=$api_key

# Run your CLI tool when the container launches
ENTRYPOINT ["python", "/usr/src/app/your_script.py"]

# docker build --build-arg server_url=http://example.com --build-arg api_key=yourapikey123 -t your-image-name .