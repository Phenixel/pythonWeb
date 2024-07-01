#Récupérer une image
FROM python:3.12-slim
LABEL authors="orelabk6"


#Ajouter dans un dossier / ou se site l'appli
WORKDIR /app

#copie ce qu'on a besoin de la machine local(projet) vers image
COPY app.py requirements.txt /app/


#Installer les Requirements.txt
RUN pip install -r requirements.txt


#ajouter un port
EXPOSE 3002

#Ajouter les varaibles d'environnement

#pour lancer l'appli
CMD ["python","app.py"]