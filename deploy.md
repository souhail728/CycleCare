# 🚀 Guide de Déploiement - CycleCare

Ce guide vous explique comment déployer l'application CycleCare sur différentes plateformes.

## 📋 Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)
- Git (optionnel, pour le versioning)

## 🏠 Déploiement Local

### Installation Rapide
```bash
# 1. Télécharger le projet
git clone <repository-url>
cd proger

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python run.py
```

### Tests
```bash
# Exécuter les tests
python test_basic.py
```

## ☁️ Déploiement Cloud

### Heroku

1. **Préparer les fichiers**
```bash
# Créer un Procfile
echo "web: python app.py" > Procfile

# Créer runtime.txt
echo "python-3.9.13" > runtime.txt
```

2. **Déployer sur Heroku**
```bash
# Installer Heroku CLI
# Puis :
heroku create cyclecare-app
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-super-secret-key-here
git push heroku main
```

### PythonAnywhere

1. **Uploader les fichiers** via l'interface web
2. **Configurer l'application** dans l'onglet Web
3. **Définir les variables d'environnement** :
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key`

### DigitalOcean App Platform

1. **Créer app.yaml**
```yaml
name: cyclecare
services:
- name: web
  source_dir: /
  github:
    repo: your-username/cyclecare
    branch: main
  run_command: python run.py
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  envs:
  - key: FLASK_ENV
    value: production
  - key: SECRET_KEY
    value: your-secret-key
```

## 🐳 Déploiement Docker

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "run.py"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  cyclecare:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-secret-key
    volumes:
      - ./data:/app/data
```

### Commandes Docker
```bash
# Construire l'image
docker build -t cyclecare .

# Lancer le conteneur
docker run -p 5000:5000 -e FLASK_ENV=production cyclecare

# Avec Docker Compose
docker-compose up -d
```

## 🔧 Configuration de Production

### Variables d'Environnement
```bash
export FLASK_ENV=production
export SECRET_KEY=your-very-secure-secret-key
export DATABASE_URL=sqlite:///production.db
```

### Sécurité
- Changez la `SECRET_KEY` par défaut
- Utilisez HTTPS en production
- Configurez un reverse proxy (Nginx)
- Activez les logs de sécurité

### Base de Données
```python
# Pour PostgreSQL
pip install psycopg2-binary
export DATABASE_URL=postgresql://user:password@localhost/cyclecare

# Pour MySQL
pip install PyMySQL
export DATABASE_URL=mysql://user:password@localhost/cyclecare
```

## 📊 Monitoring

### Logs
```bash
# Voir les logs en temps réel
tail -f app.log

# Logs avec systemd
journalctl -u cyclecare -f
```

### Santé de l'Application
```bash
# Vérifier que l'app répond
curl -I http://localhost:5000

# Endpoint de santé (à ajouter)
curl http://localhost:5000/health
```

## 🔄 Mise à Jour

### Déploiement Continu
```bash
# Script de mise à jour
#!/bin/bash
git pull origin main
pip install -r requirements.txt
python test_basic.py
sudo systemctl restart cyclecare
```

### Sauvegarde
```bash
# Sauvegarder la base de données
cp menstrual_cycle.db backup_$(date +%Y%m%d).db

# Restaurer
cp backup_20240101.db menstrual_cycle.db
```

## 🚨 Dépannage

### Problèmes Courants

1. **Port déjà utilisé**
```bash
# Trouver le processus
lsof -i :5000
# Tuer le processus
kill -9 <PID>
```

2. **Erreur de base de données**
```bash
# Recréer la base
rm menstrual_cycle.db
python -c "from app import db; db.create_all()"
```

3. **Erreur de dépendances**
```bash
# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### Logs d'Erreur
```python
# Activer les logs détaillés
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

- Vérifiez les logs d'erreur
- Consultez la documentation Flask
- Testez en local avant le déploiement
- Utilisez les tests automatisés

---

**Bonne chance avec votre déploiement ! 🚀**
