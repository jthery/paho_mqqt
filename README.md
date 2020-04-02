### paho_mqqt
Utilisation de Mosquitto pour communiquer avec des objets connectés.

### Pré-requis:
- [J'ai installé Mosquitto](https://mosquitto.org/download/)
- J'ai ajouté les variables d'environnements pointant sur le dossier Mosquitto.

### Informations:
- protocole MQTT = Message Queuing Telemetry Transport
- le cours du prof se trouve dans se Github


### Outils en ligne de commande :
- mosquitto_pub : publication de messages dans un topic
- mosquitto_sub : abonnement à un topic

### Example pour s'abonner à un topic :
```
mosquitto_sub -h mqqt.eclipse.org -t nomdutopic/souschemindutopicnonobligatoire
```
donc :
```
mosquitto_sub -h mqqt.eclipse.org -t foo
```
ou
```
mosquitto_sub -h mqqt.eclipse.org -t foo/jeremy
mosquitto_sub -h mqqt.eclipse.org -t foo/+
mosquitto_sub -h mqqt.eclipse.org -t foo/#
mosquitto_sub -h mqqt.eclipse.org -t foo/jeremy/perso
```

etc.. etc..

Donc là, c'est juste pour s'abonner à un topic.

### Example pour publier sur un topic :

```
mosquitto_pub -h mqtt.eclipse.org -t foo/jeremy -m "j'aime les fruits et légumes"
```

le -m permet de publier son message.



