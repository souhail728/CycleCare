# 🚂 CycleCare - Déploiement Railway Express

## ⚡ Déploiement en 5 Minutes

### 1. Prérequis (2 min)
- ✅ Compte [Railway](https://railway.app) (gratuit)
- ✅ Compte [GitHub](https://github.com) (gratuit)

### 2. Préparation (1 min)
```bash
# Générer une clé secrète
python generate_secret_key.py
# Copiez la SECRET_KEY affichée
```

### 3. Déploiement (2 min)

#### Option A : GitHub (Recommandé)
1. **Push vers GitHub** (si pas déjà fait)
2. **Railway** → New Project → Deploy from GitHub
3. **Sélectionner** votre repository
4. **Variables** → Ajouter :
   ```
   SECRET_KEY=votre-clé-copiée-étape-2
   FLASK_ENV=production
   RAILWAY_ENVIRONMENT=production
   ```

#### Option B : CLI Automatique
```bash
python deploy_railway.py
```

### 4. Vérification (30 sec)
- ✅ **Logs** : Pas d'erreurs
- ✅ **URL** : Application accessible
- ✅ **Health** : `/health` retourne "healthy"

## 🎯 URLs Importantes

### Votre Application
```
https://votre-app-name.up.railway.app
```

### Endpoints de Test
```
https://votre-app-name.up.railway.app/health
https://votre-app-name.up.railway.app/api/cycle_data
```

## 🔧 Variables d'Environnement

### Obligatoires
```env
SECRET_KEY=8NK726iL9ewAhYZgcsIOVkfmyugvyiaXanMABqAGXKM
FLASK_ENV=production
RAILWAY_ENVIRONMENT=production
```

### Optionnelles
```env
PORT=8080
DATABASE_URL=sqlite:///data/menstrual_cycle.db
```

## 🚨 Dépannage Express

### Application ne démarre pas
```bash
# Voir les logs
railway logs

# Vérifier les variables
railway variables
```

### Erreur 500
1. Vérifiez la `SECRET_KEY`
2. Consultez les logs Railway
3. Testez `/health` endpoint

### Base de données vide
- Normal au premier déploiement
- Se crée automatiquement au premier accès

## 💰 Coûts Railway

### Gratuit (500h/mois)
- ✅ Parfait pour CycleCare
- ✅ Domaine Railway inclus
- ✅ SSL automatique

### Pro ($5/mois)
- ✅ Illimité
- ✅ Domaine personnalisé
- ✅ Plus de ressources

## 🎉 Félicitations !

Votre application CycleCare est maintenant **en ligne** et accessible dans le monde entier !

### Prochaines Étapes
1. **Testez** toutes les fonctionnalités
2. **Partagez** l'URL avec vos utilisateurs
3. **Surveillez** les logs Railway
4. **Sauvegardez** régulièrement

---

**Support** : Consultez `RAILWAY_DEPLOY.md` pour plus de détails
