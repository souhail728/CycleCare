# 🌸 CycleCare - Guide d'Installation Rapide

## 🚀 Démarrage Rapide

### 1. Prérequis
- Python 3.9 ou supérieur installé
- Connexion Internet pour télécharger les dépendances

### 2. Installation
```bash
# Naviguer vers le dossier du projet
cd proger

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Lancement
```bash
# Lancer l'application
python run.py
```

### 4. Accès
Ouvrez votre navigateur et allez sur : **http://127.0.0.1:8080**

## ✨ Fonctionnalités Principales

### 🏠 Page d'Accueil
- **Tableau de bord** avec phase actuelle du cycle
- **Prédictions** de la prochaine période et ovulation
- **Fenêtre fertile** avec indicateurs visuels
- **Statistiques** du dernier cycle

### ➕ Ajout de Cycle
- **Formulaire intuitif** pour enregistrer un nouveau cycle
- **Validation en temps réel** des données
- **Prédictions automatiques** basées sur les informations saisies
- **Conseils personnalisés** pour un suivi optimal

### 📅 Calendrier
- **Vue calendrier interactive** avec code couleur
- **Visualisation** des périodes, ovulation et fenêtres fertiles
- **Détails au clic** sur chaque jour
- **Navigation** entre les mois

### 📊 Historique
- **Liste complète** de tous les cycles enregistrés
- **Statistiques avancées** : durée moyenne, régularité
- **Analyse des tendances** et patterns
- **Détails expandables** pour chaque cycle

## 🎨 Interface et Design

### Effets 3D Modernes
- **Cartes avec effets 3D** et animations fluides
- **Boutons interactifs** avec effets de survol
- **Gradients colorés** et design moderne
- **Animations CSS** pour une expérience riche

### Responsive Design
- **Compatible mobile** et tablette
- **Bootstrap 5** pour une interface adaptative
- **Icônes Font Awesome** pour une meilleure lisibilité

## 🔧 Calculs et Algorithmes

### Prédiction de l'Ovulation
- **Méthode du calendrier** : Ovulation = Début du cycle + (Durée du cycle - 14 jours)
- **Fenêtre fertile** : 5 jours avant l'ovulation + 1 jour après

### Analyse de la Régularité
- **Calcul automatique** de la durée moyenne des cycles
- **Évaluation de la régularité** basée sur l'écart-type
- **Prédictions futures** adaptées aux données historiques

## 🛠️ Structure du Projet

```
proger/
├── app.py                 # Application Flask principale
├── run.py                 # Script de lancement
├── requirements.txt       # Dépendances Python
├── config.py             # Configuration
├── test_basic.py         # Tests automatisés
├── menstrual_cycle.db    # Base de données (créée automatiquement)
├── templates/            # Templates HTML
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── add_cycle.html    # Formulaire d'ajout
│   ├── calendar.html     # Calendrier
│   └── history.html      # Historique
└── static/               # Fichiers statiques
    ├── css/style.css     # Styles CSS 3D
    └── js/main.js        # JavaScript
```

## 🧪 Tests

Pour exécuter les tests automatisés :
```bash
python test_basic.py
```

## 🔒 Sécurité et Confidentialité

- **Stockage local** : Toutes les données restent sur votre ordinateur
- **Base de données SQLite** : Pas de connexion externe requise
- **Validation des données** : Protection contre les entrées malveillantes
- **Sessions sécurisées** : Gestion sécurisée des sessions utilisateur

## 🆘 Dépannage

### Problème de Port
Si le port 8080 est occupé, modifiez le port dans `run.py` :
```python
port = 8081  # ou un autre port libre
```

### Erreur de Dépendances
```bash
# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### Base de Données Corrompue
```bash
# Supprimer et recréer la base
rm menstrual_cycle.db
python run.py
```

## 📱 Utilisation Recommandée

1. **Enregistrez régulièrement** vos cycles pour des prédictions précises
2. **Notez vos symptômes** pour identifier des patterns
3. **Consultez le calendrier** pour une vue d'ensemble
4. **Analysez l'historique** pour comprendre vos tendances
5. **Consultez un professionnel** en cas d'irrégularités

## 🎯 Conseils d'Utilisation

- **Soyez régulière** dans la saisie des données
- **Utilisez les notes** pour enregistrer des symptômes spécifiques
- **Consultez les prédictions** mais restez à l'écoute de votre corps
- **Sauvegardez** régulièrement votre base de données

## 📞 Support

En cas de problème :
1. Vérifiez que Python est correctement installé
2. Assurez-vous que toutes les dépendances sont installées
3. Consultez les messages d'erreur dans le terminal
4. Redémarrez l'application si nécessaire

---

**Profitez de CycleCare pour un suivi optimal de votre cycle menstruel ! 🌸**

*Développé avec ❤️ pour votre bien-être*
