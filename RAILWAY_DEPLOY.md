# 🚂 Déploiement CycleCare sur Railway

## 📋 Prérequis

1. **Compte Railway** : Créez un compte sur [railway.app](https://railway.app)
2. **Compte GitHub** : Pour connecter votre repository
3. **Code source** : Votre projet CycleCare

## 🚀 Méthodes de Déploiement

### Méthode 1 : Déploiement via GitHub (Recommandé)

#### 1. Préparer le Repository GitHub
```bash
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "Initial commit - CycleCare app"

# Ajouter le remote GitHub
git remote add origin https://github.com/votre-username/cyclecare.git

# Push vers GitHub
git push -u origin main
```

#### 2. Déployer sur Railway
1. Allez sur [railway.app](https://railway.app)
2. Cliquez sur **"New Project"**
3. Sélectionnez **"Deploy from GitHub repo"**
4. Choisissez votre repository **cyclecare**
5. Railway détectera automatiquement que c'est une app Python

#### 3. Configuration des Variables d'Environnement
Dans le dashboard Railway, allez dans **Variables** et ajoutez :
```
FLASK_ENV=production
SECRET_KEY=votre-cle-secrete-super-longue-et-complexe
RAILWAY_ENVIRONMENT=production
```

### Méthode 2 : Déploiement via Railway CLI

#### 1. Installer Railway CLI
```bash
# Windows (avec npm)
npm install -g @railway/cli

# Ou télécharger depuis https://railway.app/cli
```

#### 2. Login et Déploiement
```bash
# Se connecter à Railway
railway login

# Initialiser le projet
railway init

# Déployer
railway up
```

### Méthode 3 : Déploiement Direct (Upload)

1. Compressez votre dossier projet en ZIP
2. Allez sur Railway → **New Project** → **Deploy from Template**
3. Uploadez votre fichier ZIP

## ⚙️ Configuration Railway

### Variables d'Environnement Recommandées
```env
# Obligatoires
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
RAILWAY_ENVIRONMENT=production

# Optionnelles
PORT=8080
DATABASE_URL=sqlite:///data/menstrual_cycle.db
```

### Génération d'une Clé Secrète Sécurisée
```python
# Exécutez ce code pour générer une clé secrète
import secrets
print(secrets.token_urlsafe(32))
```

## 🔧 Fichiers de Configuration Créés

### `Procfile`
```
web: python start.py
```

### `runtime.txt`
```
python-3.9.18
```

### `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python start.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

## 📊 Monitoring et Logs

### Voir les Logs
```bash
# Via CLI
railway logs

# Ou dans le dashboard Railway → Deployments → View Logs
```

### Métriques
- **CPU Usage** : Visible dans le dashboard
- **Memory Usage** : Monitoring automatique
- **Request Count** : Statistiques de trafic

## 🔒 Sécurité en Production

### Variables d'Environnement Sécurisées
- ✅ `SECRET_KEY` : Clé secrète forte
- ✅ `FLASK_ENV=production` : Mode production
- ✅ Cookies sécurisés activés automatiquement

### Base de Données
- **SQLite** : Stockage persistant sur Railway
- **Backup automatique** : Railway sauvegarde automatiquement
- **Volume persistant** : Les données survivent aux redéploiements

## 🌐 Domaine Personnalisé

### Domaine Railway (Gratuit)
Votre app sera accessible sur : `https://votre-app-name.up.railway.app`

### Domaine Personnalisé (Pro)
1. Allez dans **Settings** → **Domains**
2. Ajoutez votre domaine personnalisé
3. Configurez les DNS selon les instructions

## 🚨 Dépannage

### Erreurs Communes

#### 1. Application ne démarre pas
```bash
# Vérifier les logs
railway logs

# Vérifier les variables d'environnement
railway variables
```

#### 2. Base de données vide
```bash
# Se connecter au shell Railway
railway shell

# Recréer la base
python -c "from app import db; db.create_all()"
```

#### 3. Erreur de port
Assurez-vous que votre app utilise `os.environ.get('PORT', 8080)`

### Commandes Utiles
```bash
# Status du déploiement
railway status

# Redéployer
railway up

# Variables d'environnement
railway variables

# Shell interactif
railway shell

# Ouvrir l'app
railway open
```

## 💰 Coûts Railway

### Plan Gratuit
- **500 heures d'exécution/mois**
- **1 GB RAM**
- **1 GB stockage**
- **Domaine Railway gratuit**

### Plan Pro ($5/mois)
- **Exécution illimitée**
- **8 GB RAM**
- **100 GB stockage**
- **Domaines personnalisés**

## 🎯 Optimisations

### Performance
- **Gunicorn** : Pour la production (optionnel)
- **Redis** : Pour le cache (si nécessaire)
- **CDN** : Pour les assets statiques

### Monitoring
- **Sentry** : Pour le tracking d'erreurs
- **Analytics** : Google Analytics ou similaire

## ✅ Checklist de Déploiement

- [ ] Repository GitHub créé et pushé
- [ ] Variables d'environnement configurées
- [ ] `SECRET_KEY` générée et sécurisée
- [ ] Application testée localement
- [ ] Déploiement Railway effectué
- [ ] Logs vérifiés (pas d'erreurs)
- [ ] Application accessible via l'URL Railway
- [ ] Fonctionnalités testées en production

## 🎉 Félicitations !

Votre application CycleCare est maintenant déployée sur Railway ! 

**URL d'accès** : `https://votre-app-name.up.railway.app`

---

**Support Railway** : [docs.railway.app](https://docs.railway.app)
**Support CycleCare** : Consultez les logs pour le dépannage
