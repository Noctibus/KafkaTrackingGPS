# KafkaTrackingGPS


## Kafka configuration
Dans le dossier ```kafka``` se trouvent :
- ```config.py``` : fichier de configuration contenant les variables à importer pour ne pas avoir à les modifier dans chacun des fichiers où elles sont utilisées
- ```consumer.py``` : dans ce fichier se trouve la fonction à appeler et éxécuter pour lire les messages dans Kafka. Elle doit éxécuter une fonction qu'il faut écrire ou importer. Example : insertion dans BDD, envoie au front...
- ```docker-compose.yml``` : fichier de configuration du docker Kafka : Kafka & Kafka UI
- ```producer.py``` : dans ce fichier se trouve la fonction à éxécuter pour envoyer les données à Kafka. Requiert : id (int), latitude (float), longitude (float).
