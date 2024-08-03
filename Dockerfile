# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Nginx and other dependencies
RUN apt-get update && \
    apt-get install -y nginx && \
    python -m venv venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Collect static files and run migrations
RUN /venv/bin/python manage.py collectstatic --noinput && \
    /venv/bin/python manage.py migrate

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and Gunicorn
CMD ["sh", "-c", "service nginx start && /venv/bin/gunicorn tech_ocean_institute.wsgi:application --bind 0.0.0.0:8000"]
