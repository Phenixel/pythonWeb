# Utiliser l'image officielle de Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et app.py dans le répertoire de travail
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Vérifier que Flask est installé
RUN pip show Flask

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Définir la commande pour exécuter l'application Flask
CMD ["python", "app.py"]
