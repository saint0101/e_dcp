# Use the PHP with Apache image
FROM php:7.4-apache

# Set the working directory to /var/www/html
WORKDIR /var/www/html

# Copy the contents of the local directory /e_dcp/frontend/www into the container
COPY www/ .

# Expose port 80 for web traffic
EXPOSE 80