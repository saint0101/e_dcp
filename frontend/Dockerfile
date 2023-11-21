# Use the PHP with Apache image
FROM php:7.4-apache

# Set the working directory to /var/www/html
WORKDIR /e_dcpf/frontend/www

RUN ls .

# Copy the index.html file into the container
COPY . /var/www/html/

# Expose port 80 for web traffic
EXPOSE 80

