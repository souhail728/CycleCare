#!/usr/bin/env python3
"""
Script de déploiement automatisé pour Railway
"""
import os
import subprocess
import sys
import json

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès")
            return True
        else:
            print(f"❌ {description} - Erreur:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erreur lors de {description}: {e}")
        return False

def check_railway_cli():
    """Vérifie si Railway CLI est installé"""
    result = subprocess.run("railway --version", shell=True, capture_output=True)
    return result.returncode == 0

def check_git():
    """Vérifie si Git est installé et configuré"""
    result = subprocess.run("git --version", shell=True, capture_output=True)
    return result.returncode == 0

def main():
    """Fonction principale de déploiement"""
    print("🚂 Script de Déploiement CycleCare sur Railway")
    print("=" * 50)
    
    # Vérifications préliminaires
    print("🔍 Vérifications préliminaires...")
    
    if not check_git():
        print("❌ Git n'est pas installé ou configuré")
        print("💡 Installez Git depuis: https://git-scm.com/")
        return False
    
    if not check_railway_cli():
        print("❌ Railway CLI n'est pas installé")
        print("💡 Installez Railway CLI:")
        print("   npm install -g @railway/cli")
        print("   ou téléchargez depuis: https://railway.app/cli")
        return False
    
    print("✅ Vérifications préliminaires - OK")
    print()
    
    # Tests locaux
    print("🧪 Tests locaux...")
    if not run_command("python test_basic.py", "Exécution des tests"):
        print("⚠️  Les tests ont échoué, mais on continue...")
    print()
    
    # Préparation Git
    print("📦 Préparation du repository...")
    
    # Vérifier si c'est déjà un repo Git
    if not os.path.exists('.git'):
        if not run_command("git init", "Initialisation Git"):
            return False
    
    # Ajouter les fichiers
    if not run_command("git add .", "Ajout des fichiers"):
        return False
    
    # Commit
    commit_message = input("💬 Message de commit (ou Entrée pour défaut): ").strip()
    if not commit_message:
        commit_message = "Deploy CycleCare to Railway"
    
    if not run_command(f'git commit -m "{commit_message}"', "Commit des changements"):
        print("ℹ️  Aucun changement à committer ou commit déjà effectué")
    
    print()
    
    # Déploiement Railway
    print("🚂 Déploiement sur Railway...")
    
    # Login Railway (si nécessaire)
    print("🔐 Vérification de l'authentification Railway...")
    result = subprocess.run("railway whoami", shell=True, capture_output=True)
    if result.returncode != 0:
        print("🔑 Connexion à Railway requise...")
        if not run_command("railway login", "Connexion Railway"):
            return False
    
    # Initialiser le projet Railway (si nécessaire)
    if not os.path.exists('.railway'):
        print("🆕 Initialisation du projet Railway...")
        if not run_command("railway init", "Initialisation Railway"):
            return False
    
    # Déploiement
    if not run_command("railway up", "Déploiement sur Railway"):
        return False
    
    print()
    print("🎉 Déploiement terminé avec succès!")
    print()
    
    # Informations post-déploiement
    print("📋 Prochaines étapes:")
    print("1. Configurez les variables d'environnement dans Railway:")
    print("   - SECRET_KEY=<votre-clé-secrète>")
    print("   - FLASK_ENV=production")
    print("   - RAILWAY_ENVIRONMENT=production")
    print()
    print("2. Générez une clé secrète avec:")
    print("   python generate_secret_key.py")
    print()
    print("3. Vérifiez les logs avec:")
    print("   railway logs")
    print()
    print("4. Ouvrez votre application avec:")
    print("   railway open")
    
    return True

if __name__ == '__main__':
    try:
        success = main()
        if success:
            print("\n🚀 Déploiement réussi!")
            sys.exit(0)
        else:
            print("\n💥 Déploiement échoué!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️  Déploiement annulé par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        sys.exit(1)
