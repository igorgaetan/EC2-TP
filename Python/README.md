# Projet — Déploiement d'une application Python sur AWS EC2 (via User Data)

## 🎯 Objectif

Déployer une application web Python (Flask) sur une instance **EC2**, en utilisant
**exclusivement un script `user-data`** exécuté automatiquement au démarrage de
l'instance. L'application doit être **directement accessible dans un navigateur**
dès que l'instance est lancée, **sans connexion SSH**.

## 📦 Fichiers fournis

- `app.py` : l'application Flask (frontend simple, ne pas modifier la logique).
- `requirements.txt` : les dépendances Python nécessaires.

Ces deux fichiers doivent être présents sur l'instance EC2 pour que l'application
puisse démarrer (à vous de trouver comment les y faire parvenir, cf. contraintes).

## 📋 Consignes

1. Récupérez les fichiers `app.py` et `requirements.txt` de ce projet.
2. Écrivez un script **`user-data`** (bash) qui, exécuté automatiquement au
   premier démarrage de l'instance, doit :
   - installer Python 3 et pip (et tout autre paquet nécessaire) ;
   - récupérer les fichiers de l'application sur l'instance;
   - installer les dépendances (`requirements.txt`) ;
   - lancer l'application `app.py` **au démarrage du serveur**.
3. Créez une instance EC2 (Amazon Linux ou Ubuntu, à votre choix) et collez
   votre script dans le champ **"User data"** au moment du lancement.
4. Configurez le **Security Group** de l'instance pour autoriser le trafic
   entrant sur le port utilisé par l'application (voir `app.py`).
5. Une fois l'instance démarrée (laissez-lui 1 à 2 minutes), ouvrez un
   navigateur et accédez à :

   ```
   http://<IP_PUBLIQUE_DE_L_INSTANCE>:<PORT>
   ```

6. Vérifiez que la page s'affiche correctement, avec le message de succès,
   le nom du serveur et l'heure.

## ⚠️ Contraintes obligatoires

- ❌ **Aucune connexion SSH** ne doit être utilisée pour déployer ou démarrer
  l'application. Tout doit passer par le script **user-data**.
- ✅ L'application doit démarrer **automatiquement** avec l'instance (si on
  redémarre l'instance, l'application doit idéalement redémarrer aussi).
- ✅ L'URL utilisée pour accéder à l'application doit clairement afficher
  **l'IP publique ET le port** de l'instance.
- ✅ Ne modifiez pas la logique de `app.py` : le but de l'exercice est le
  déploiement, pas le développement front-end.

## 📤 Livrable

Une **capture d'écran** de votre navigateur affichant l'application en cours
d'exécution, sur laquelle on doit voir clairement :

- la **barre d'adresse** avec l'IP publique et le port de l'instance EC2 ;
- le contenu de la page (message de succès, nom du serveur, heure).

## 🧪 Tester en local (optionnel, avant le déploiement)

```bash
pip install -r requirements.txt
python app.py
```

Puis ouvrez `http://localhost:5000` dans votre navigateur.
