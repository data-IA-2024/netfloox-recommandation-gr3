# Netfloox


## Installation

1.  Création de l'environnement virtuel

```bash
python3 -m venv .venv
```

2. Activation de l'environnement virtuel (Linux/MacOS)

```bash
source .venv/bin/activate
```

3. Installation des dépendances

```bash
pip install -r requirements.txt
```

## Connexion base de données
Les paramétres de connexion à la base de données doivent être mis dans un fichier `.env` (cf. `.env_template`).  
```bash
# fichier .env

DB_HOST="database_host"
DB_PORT="server_port"
DB_USER="username"
DB_PASS="password"
DB_NAME="database_name"
```

## Dataset
ImDB [data](https://developer.imdb.com/non-commercial-datasets)