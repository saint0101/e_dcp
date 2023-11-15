# Utiliser l'image officielle Apache avec PHP
FROM php:7.1-apache

# Installer git pour pouvoir cloner le dépôt GitHub
RUN apt-get update && apt-get install -y git

# Cloner le dépôt GitHub contenant le site de test
RUN git clone -b test https://github.com/saint0101/e_dcp.git

WORKDIR /e_dcp/frontend/www

COPY www/index.html /var/www/html

# Optionnel : Exposer le port 80
EXPOSE 80

# Start Apache when the container launches
CMD ["apache2-foreground"]