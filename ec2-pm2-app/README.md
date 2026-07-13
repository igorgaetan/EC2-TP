# Exercice — Déploiement automatisé d'une application Node.js sur EC2

## 🎯 Objectif

Déployer l'application frontend fournie dans ce dépôt sur une instance **AWS EC2**, de manière **entièrement automatisée**, sans jamais vous connecter en SSH à la machine.

À la fin de l'exercice, l'application doit être **accessible directement dans un navigateur** dès que l'instance EC2 a fini de démarrer, et doit **rester disponible même après un redémarrage** de l'instance.

## 📦 Contenu du dépôt

```
.
├── app.js              # Serveur Express qui sert le frontend
├── package.json        # Dépendances de l'application
├── public/
│   └── index.html      # Page frontend
└── README.md            # Ce fichier
```

L'application écoute par défaut sur le **port 3000**.

## 🚧 Contraintes obligatoires

1. **Aucun accès SSH** n'est autorisé pour effectuer le déploiement. Toute l'installation et le démarrage de l'application doivent passer par le **user-data** de l'instance EC2.
2. L'application doit être démarrée avec **pm2**.
3. L'application doit démarrer **automatiquement**, sans intervention manuelle, dès que l'instance EC2 est disponible (y compris après un `reboot` ou un arrêt/redémarrage de l'instance).
4. Le **Security Group** de l'instance doit autoriser le trafic entrant sur le port utilisé par l'application (ex. 3000), en plus du port 80 si vous choisissez de faire un reverse proxy (facultatif, non obligatoire pour cet exercice).

## 🧩 Ce que votre script user-data doit accomplir

Vous devez écrire vous-même le script **user-data** (bash) à coller dans le champ *User data* lors du lancement de l'instance EC2. Il doit, au minimum :

- Installer les paquets système nécessaires (Node.js, npm, git...).
- Récupérer le code de l'application sur l'instance (dépôt git, ou tout autre moyen ne nécessitant pas de SSH manuel).
- Installer les dépendances de l'application (`npm install`).
- Installer **pm2** globalement.
- Démarrer l'application avec **pm2**.
- Configurer pm2 pour qu'il **relance automatiquement l'application au démarrage du système** (indice : regardez du côté de `pm2 startup` et `pm2 save`).

> 💡 Réfléchissez à l'utilisateur sous lequel le script user-data s'exécute (par défaut `root`), cela a un impact sur la commande `pm2 startup` à utiliser.

## ✅ Livrable attendu

Une **capture d'écran** de l'application ouverte dans un navigateur web, sur laquelle on doit clairement voir dans la barre d'adresse :

- l'**adresse IP publique** de l'instance EC2,
- le **port** utilisé par l'application.

Exemple de format attendu dans la barre d'adresse : `http://<IP_PUBLIQUE_EC2>:<PORT>`

Aucune autre preuve (logs, terminal, etc.) n'est requise — seule la capture d'écran du navigateur sera évaluée.

## 🧪 Pour tester en local (facultatif, avant le déploiement)

```bash
npm install
node app.js
```

Puis ouvrez `http://localhost:3000` dans votre navigateur.
