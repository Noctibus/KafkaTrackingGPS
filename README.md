# KafkaTrackingGPS
## Suivi en direct des coordonnées lors d'un déplacement

Lancement :
- `docker-compose up --build` : démarrer les docker (kafka, database, angular). Il est possible de démarrer Kafka UI et phpmyadmin en retirant les commentaires associés.
- `pip install -r kafka/requirements.txt` : installer les paquets python nécessaires au lancement du producer.
- `python kafka/producer.py` : lancement du consumer pour reccueillir les données de Kafka et les insérer dans une BDD.
- ouvrir une page web à l'adresse [http://localhost:4200](http://localhost:4200)

Vous êtes prêts à voir évoluer la position.

Pour lancer la génération de coordonnées, lancer le script producer.py :
- `python kafka/producer.py n`, avec n=1 ou n=2 : c'est le choix d'une adresse ip.
