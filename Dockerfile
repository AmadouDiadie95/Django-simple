FROM ubuntu

# Etiquette pour le mainteneur
LABEL maintainer="amadou.diadie04@gmail.com"

COPY . /Daamtu/Django-simple

RUN apt-get update
RUN apt-get install -y curl neofetch iputils-ping nano btop

# Copy and set permissions for the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command (keeps the container running)
CMD ["sleep", "500000000"]
