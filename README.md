# 🌸 CycleCare - Système de Suivi du Cycle Menstruel

Une application web moderne et élégante pour le suivi du cycle menstruel avec des effets 3D et une interface utilisateur intuitive.

## ✨ Fonctionnalités

### 🏠 Tableau de Bord Principal
- **Phase actuelle du cycle** avec indicateurs visuels
- **Prédiction de la prochaine période** menstruelle
- **Calcul automatique de l'ovulation** (méthode du calendrier)
- **Fenêtre fertile** avec indicateurs en temps réel
- **Statistiques du dernier cycle** enregistré

### ➕ Ajout de Cycles
- Formulaire intuitif pour enregistrer un nouveau cycle
- **Prédictions en temps réel** basées sur les données saisies
- Validation des données avec messages d'erreur clairs
- **Conseils personnalisés** pour un suivi optimal

### 📅 Calendrier Visuel
- **Calendrier interactif** avec code couleur
- Visualisation des périodes menstruelles, ovulation et fenêtres fertiles
- **Informations détaillées** au clic sur chaque jour
- **Prochains événements** prédits

### 📊 Historique et Statistiques
- **Historique complet** de tous les cycles enregistrés
- **Statistiques avancées** : durée moyenne, régularité
- **Analyse de la régularité** des cycles
- **Symptômes et humeurs** les plus fréquents

## 🎨 Design et Interface

### Effets 3D Modernes
- **Cartes avec effets 3D** et animations fluides
- **Boutons interactifs** avec effets de survol
- **Gradients colorés** et thème moderne
- **Animations CSS** pour une expérience utilisateur riche

### Responsive Design
- **Compatible mobile** et tablette
- **Bootstrap 5** pour une interface adaptative
- **Icônes Font Awesome** pour une meilleure lisibilité

## 🚀 Installation et Lancement

### Prérequis
- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation
1. **Cloner ou télécharger** le projet
2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Lancement
```bash
python app.py
```
ou
```bash
python run.py
```

L'application sera accessible sur : **http://127.0.0.1:8080**

## 🚂 Déploiement sur Railway (Cloud)

### Déploiement Rapide
```bash
# 1. Générer une clé secrète
python generate_secret_key.py

# 2. Déploiement automatisé
python deploy_railway.py
```

### Déploiement Manuel
1. **Créer un compte** sur [railway.app](https://railway.app)
2. **Connecter votre repository** GitHub
3. **Configurer les variables d'environnement** :
   - `SECRET_KEY=votre-clé-secrète`
   - `FLASK_ENV=production`
   - `RAILWAY_ENVIRONMENT=production`
4. **Déployer** automatiquement

**Consultez** `RAILWAY_DEPLOY.md` pour le guide complet.

## 📁 Structure du Projet

```
proger/
├── app.py                 # Application Flask principale
├── run.py                 # Script de lancement
├── requirements.txt       # Dépendances Python
├── menstrual_cycle.db    # Base de données SQLite (créée automatiquement)
├── templates/            # Templates HTML
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── add_cycle.html    # Formulaire d'ajout
│   ├── calendar.html     # Calendrier interactif
│   └── history.html      # Historique des cycles
└── static/               # Fichiers statiques
    ├── css/
    │   └── style.css     # Styles CSS 3D personnalisés
    └── js/
        └── main.js       # JavaScript pour les interactions
```

## 🔧 Technologies Utilisées

### Backend
- **Flask 2.3.3** - Framework web Python
- **SQLAlchemy** - ORM pour la base de données
- **SQLite** - Base de données légère
- **Python-dateutil** - Manipulation des dates

### Frontend
- **Bootstrap 5** - Framework CSS responsive
- **Font Awesome 6** - Icônes vectorielles
- **CSS3** - Effets 3D et animations
- **JavaScript ES6** - Interactions dynamiques

## 📊 Calculs et Algorithmes

### Prédiction de l'Ovulation
- **Méthode du calendrier** : Ovulation = Début du cycle + (Durée du cycle - 14 jours)
- **Fenêtre fertile** : 5 jours avant l'ovulation + 1 jour après

### Analyse de la Régularité
- **Calcul de la durée moyenne** des cycles
- **Écart-type** pour déterminer la régularité
- **Classification** : Régulier (≤2j), Irrégulier (2-4j), Très irrégulier (>4j)

### Prédictions Futures
- **Prédiction des 6 prochains cycles** basée sur les données historiques
- **Adaptation automatique** selon la durée moyenne des cycles

## 🎯 Fonctionnalités Avancées

### API REST
- `/api/cycle_data` - Données des cycles au format JSON
- `/api/predictions` - Prédictions des prochains cycles
- `/api/stats` - Statistiques détaillées

### Validation des Données
- **Validation côté client** avec JavaScript
- **Validation côté serveur** avec Flask-WTF
- **Messages d'erreur** contextuels et informatifs

### Expérience Utilisateur
- **Animations fluides** et transitions CSS
- **Tooltips informatifs** sur les éléments interactifs
- **Feedback visuel** pour toutes les actions utilisateur

## 🔒 Sécurité et Confidentialité

- **Stockage local** des données (pas de cloud)
- **Base de données SQLite** chiffrée par défaut
- **Validation des entrées** pour éviter les injections
- **Sessions sécurisées** avec clé secrète

## 🌟 Conseils d'Utilisation

1. **Enregistrez régulièrement** vos cycles pour des prédictions précises
2. **Notez vos symptômes** pour identifier des patterns
3. **Consultez le calendrier** pour une vue d'ensemble
4. **Utilisez l'historique** pour analyser vos tendances
5. **Consultez un professionnel** en cas d'irrégularités importantes

## 🤝 Contribution

Ce projet est ouvert aux contributions ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer le design ou l'expérience utilisateur

## 📝 Licence

Ce projet est sous licence libre. Vous pouvez l'utiliser, le modifier et le distribuer librement.

---

**Développé avec ❤️ pour le bien-être féminin**

*CycleCare - Votre compagnon pour le suivi du cycle menstruel*
