const express = require("express");
const path = require("path");

const app = express();

// Le port peut être imposé par l'étudiant via une variable d'environnement,
// mais une valeur par défaut est fournie pour simplifier l'exercice.
const PORT = process.env.PORT || 3000;

// Sert les fichiers statiques du dossier "public" (le frontend)
app.use(express.static(path.join(__dirname, "public")));

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Serveur démarré sur le port ${PORT}`);
});
