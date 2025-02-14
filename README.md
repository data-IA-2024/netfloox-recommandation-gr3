# Netfloox Groupe 3
Projet Système de recommandation de films ainsi qu'un algorithme de prédiction de popularité.


## Installation

1.  Création de l'environnement virtuel

```bash
python3 -m venv .venv
```

2. Activation de l'environnement virtuel

```bash
# Linux/MacOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Installation des dépendances

```bash
pip install -r requirements.txt
```

## Connection base de données
Les paramétres de connexion à la base de données doivent être mis dans un fichier `.env` (cf. `.env_template`) dans le dossier `config`.  
```bash
# fichier .env

DB_HOST="database_host"
DB_PORT="server_port"
DB_USER="username"
DB_PASS="password"
DB_NAME="database_name"
```

## Dataset
Données non-commercial ImDB [data](https://developer.imdb.com/non-commercial-datasets)