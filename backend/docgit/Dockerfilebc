# Utiliser une image de base avec git installé
FROM git:latest

# Spécifier le répertoire de travail dans le conteneur
WORKDIR /app

# Cloner le dépôt GitHub dans le conteneur
RUN git clone -b api_edcp1 https://github.com/saint0101/e_dcp.git .

# Utiliser l'image Python comme image de base pour la suite
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier le contenu cloné dans le répertoire de travail du conteneur
COPY --from=0 /app .

# Installer les dépendances
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Exposer le port
EXPOSE 5000

# Exécuter l'application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
