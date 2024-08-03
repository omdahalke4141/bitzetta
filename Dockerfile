# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Install Python dependencies
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Collect static files
RUN /bin/bash -c "source venv/bin/activate && python manage.py collectstatic --noinput"

# Run migrations
RUN /bin/bash -c "source venv/bin/activate && python manage.py migrate"

# Expose port 80
EXPOSE 80

# Run Nginx and Django server
CMD service nginx start && /bin/bash -c "source venv/bin/activate && gunicorn tech_ocean_institute.wsgi:application --bind 0.0.0.0:8000"
