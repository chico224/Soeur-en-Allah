# Backend Soeur en Allah

Ce backend est construit avec FastAPI et fournit les endpoints nécessaires pour l'application web Soeur en Allah.

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration

La base de données est configurée par défaut pour utiliser SQLite. Pour changer vers PostgreSQL, modifier la variable `SQLALCHEMY_DATABASE_URL` dans `database.py`.

## Lancement du serveur

```bash
uvicorn main:app --reload
```

Le serveur sera accessible sur `http://localhost:8000`

## Documentation API

La documentation interactive de l'API est disponible sur :
- Swagger UI : `http://localhost:8000/docs`
- ReDoc : `http://localhost:8000/redoc`

## Endpoints disponibles

- `/api/journal/` - Gestion du journal spirituel
- `/api/confession/` - Espace de confession
- `/api/quran/` - Accès au Coran
- `/api/goals/` - Gestion des objectifs
- `/api/books/` - Bibliothèque
- `/api/events/` - Calendrier

## Sécurité

L'authentification JWT est implémentée pour sécuriser les endpoints nécessitant une authentification.
