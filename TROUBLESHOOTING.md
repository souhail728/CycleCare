# 🚨 Guide de Dépannage CycleCare

## 🔧 Erreurs Communes et Solutions

### 1. UnboundLocalError: local variable 'today' referenced before assignment

**Symptôme** : Erreur 500 sur la page d'accueil
```
UnboundLocalError: local variable 'today' referenced before assignment
```

**Cause** : Variable `today` non initialisée dans tous les cas

**Solution** : ✅ **CORRIGÉE** dans la dernière version
```bash
# Redéployer avec la correction
python fix_and_redeploy.py
```

### 2. Application ne démarre pas sur Railway

**Symptômes** :
- Build réussi mais app ne répond pas
- Timeout lors de l'accès
- Logs montrent des erreurs de port

**Solutions** :
```bash
# 1. Vérifier les logs
railway logs

# 2. Vérifier les variables d'environnement
railway variables

# 3. Redémarrer le service
railway restart
```

**Variables requises** :
```env
SECRET_KEY=votre-clé-secrète
FLASK_ENV=production
RAILWAY_ENVIRONMENT=production
```

### 3. Erreur de Base de Données

**Symptôme** : Erreur lors de l'accès aux données
```
sqlite3.OperationalError: no such table: cycle_record
```

**Solution** :
```bash
# La base se crée automatiquement au premier accès
# Si problème persiste, redéployer
railway up
```

### 4. Erreur 404 sur les Routes

**Symptôme** : Pages non trouvées
**Cause** : Problème de routing Flask

**Solution** :
```bash
# Vérifier que toutes les routes sont définies
python -c "from app import app; print(app.url_map)"
```

### 5. Erreur de Clé Secrète

**Symptôme** : Erreur de session ou cookies
**Cause** : SECRET_KEY manquante ou invalide

**Solution** :
```bash
# Générer une nouvelle clé
python generate_secret_key.py

# L'ajouter dans Railway → Variables
```

### 6. Erreur de Template

**Symptôme** : 
```
jinja2.exceptions.TemplateNotFound: template.html
```

**Solution** :
- Vérifier que le dossier `templates/` existe
- Vérifier les noms de fichiers
- Redéployer si nécessaire

### 7. Erreur CSS/JS

**Symptôme** : Styles ou JavaScript ne se chargent pas
**Cause** : Problème avec les fichiers statiques

**Solution** :
- Vérifier le dossier `static/`
- Vérifier les URLs dans les templates
- Forcer le rechargement du cache

## 🔍 Commandes de Diagnostic

### Logs Railway
```bash
# Logs en temps réel
railway logs --follow

# Logs des dernières 100 lignes
railway logs --tail 100
```

### Status de l'Application
```bash
# Status général
railway status

# Variables d'environnement
railway variables

# Informations du projet
railway info
```

### Tests Locaux
```bash
# Tests automatisés
python test_basic.py

# Test de l'import
python -c "from app import app; print('OK')"

# Test du démarrage
python start.py
```

### Health Check
```bash
# Local
curl http://localhost:8080/health

# Railway
curl https://votre-app.up.railway.app/health
```

## 🚑 Solutions d'Urgence

### 1. Rollback Rapide
```bash
# Revenir à la version précédente
git revert HEAD
railway up
```

### 2. Redéploiement Complet
```bash
# Forcer un nouveau déploiement
railway up --detach
```

### 3. Reset de la Base de Données
```bash
# Se connecter au shell Railway
railway shell

# Recréer les tables
python -c "from app import db; db.drop_all(); db.create_all()"
```

### 4. Variables d'Environnement d'Urgence
```bash
# Définir rapidement les variables essentielles
railway variables set SECRET_KEY=nouvelle-clé-secrète
railway variables set FLASK_ENV=production
railway variables set RAILWAY_ENVIRONMENT=production
```

## 📊 Monitoring

### Métriques à Surveiller
- **CPU Usage** : < 80%
- **Memory Usage** : < 90%
- **Response Time** : < 2s
- **Error Rate** : < 1%

### Alertes Importantes
- Erreurs 500 répétées
- Timeouts fréquents
- Utilisation mémoire élevée
- Échecs de déploiement

## 🔧 Outils de Debug

### Debug Local
```python
# Activer le mode debug
export FLASK_ENV=development
python app.py
```

### Debug Railway
```bash
# Shell interactif
railway shell

# Variables d'environnement
env | grep -E "(FLASK|RAILWAY|SECRET)"
```

### Logs Détaillés
```python
# Dans app.py, ajouter temporairement
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

### Ordre de Vérification
1. **Logs Railway** - Première source d'information
2. **Variables d'environnement** - Souvent la cause
3. **Tests locaux** - Reproduire le problème
4. **Health endpoint** - Vérifier l'état de l'app
5. **Redéploiement** - Solution souvent efficace

### Ressources Utiles
- [Documentation Railway](https://docs.railway.app)
- [Documentation Flask](https://flask.palletsprojects.com)
- [Logs Railway en temps réel](https://railway.app/dashboard)

### Contact d'Urgence
En cas de problème critique :
1. Vérifiez les logs Railway
2. Testez localement
3. Utilisez `fix_and_redeploy.py`
4. Consultez ce guide de dépannage

---

**Dernière mise à jour** : Correction de l'erreur UnboundLocalError
**Status** : ✅ Application stable et fonctionnelle
