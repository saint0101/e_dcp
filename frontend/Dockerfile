# Use the PHP with Apache image
FROM php:7.4-apache

# Set the working directory to /var/www/html
WORKDIR /var/www/html

# Copier le contenu cloné dans le répertoire de travail du conteneur
COPY --from=0 www/ .

# Expose port 80 for web traffic
EXPOSE 80

# Supprimer le dépôt cloné à la fin du déploiement
RUN rm -rf /www