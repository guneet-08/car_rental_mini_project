# Use an appropriate base image with Python pre-installed
FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y mysql-server

# Copy the rest of the application files to the container
COPY . .

# Define the command to run your application
CMD ["python", "DBConnection.py"]

