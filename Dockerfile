# Utilisation d'une image de base Python 3.11
FROM python:3.11

# Etiquette pour le mainteneur
LABEL maintainer="amadou.diadie04@gmail.com"

WORKDIR /app

# Copie tout le contenu du répertoire local dans le répertoire de travail de l'image
COPY . /app

# Install the package dependencies in the requirements file.
#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Exposition du port 8000
EXPOSE 9000

# Point d'entrée pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "127.0.0.1:9000"]
