# Use an official Python runtime as a parent image
FROM python:3.10

# Define environment variable
ENV NAME World

# Set the working directory to /app
WORKDIR /app

# Copy code into container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# WORKDIR app
# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5055"]
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000", "-e", "edcp:app"]
