FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files to disk and unbuffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/

# Expose port 8000 for the Django app (this is for documentation/inter-container communication)
EXPOSE 8000

# Command to run the Django development server
# 0.0.0.0:8000 makes the server accessible from outside the container's loopback interface
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]