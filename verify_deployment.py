#!/usr/bin/env python3
"""
Script de vérification avant déploiement Railway
"""
import os
import sys
import subprocess
import importlib.util

def check_file_exists(filepath, description):
    """Vérifie qu'un fichier existe"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} manquant: {filepath}")
        return False

def check_python_import(module_name):
    """Vérifie qu'un module Python peut être importé"""
    try:
        __import__(module_name)
        print(f"✅ Import {module_name}: OK")
        return True
    except ImportError as e:
        print(f"❌ Import {module_name}: {e}")
        return False

def run_tests():
    """Exécute les tests automatisés"""
    try:
        result = subprocess.run(
            ["python", "test_basic.py"], 
            capture_output=True, 
            text=True, 
            timeout=60
        )
        if result.returncode == 0:
            print("✅ Tests automatisés: PASSÉS")
            return True
        else:
            print("❌ Tests automatisés: ÉCHEC")
            print(result.stderr)
            return False
    except subprocess.TimeoutExpired:
        print("❌ Tests automatisés: TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ Tests automatisés: ERREUR - {e}")
        return False

def check_app_startup():
    """Vérifie que l'application peut démarrer"""
    try:
        # Test d'import de l'application
        from app import app, db
        
        # Test de création du contexte
        with app.app_context():
            db.create_all()
        
        print("✅ Démarrage application: OK")
        return True
    except Exception as e:
        print(f"❌ Démarrage application: {e}")
        return False

def main():
    """Fonction principale de vérification"""
    print("🔍 Vérification de Déploiement CycleCare")
    print("=" * 50)
    
    all_checks_passed = True
    
    # 1. Vérification des fichiers essentiels
    print("\n📁 Fichiers essentiels:")
    essential_files = [
        ("app.py", "Application principale"),
        ("start.py", "Script de démarrage Railway"),
        ("requirements.txt", "Dépendances Python"),
        ("Procfile", "Configuration Railway"),
        ("runtime.txt", "Version Python"),
        ("railway.json", "Configuration Railway JSON")
    ]
    
    for filepath, description in essential_files:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    # 2. Vérification des templates
    print("\n🎨 Templates:")
    template_files = [
        ("templates/base.html", "Template de base"),
        ("templates/index.html", "Page d'accueil"),
        ("templates/add_cycle.html", "Formulaire d'ajout"),
        ("templates/calendar.html", "Calendrier"),
        ("templates/history.html", "Historique")
    ]
    
    for filepath, description in template_files:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    # 3. Vérification des fichiers statiques
    print("\n🎯 Fichiers statiques:")
    static_files = [
        ("static/css/style.css", "Styles CSS"),
        ("static/js/main.js", "JavaScript")
    ]
    
    for filepath, description in static_files:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    # 4. Vérification des dépendances Python
    print("\n🐍 Dépendances Python:")
    dependencies = ["flask", "flask_sqlalchemy"]
    
    for dep in dependencies:
        if not check_python_import(dep):
            all_checks_passed = False
    
    # 5. Test de démarrage de l'application
    print("\n🚀 Test de démarrage:")
    if not check_app_startup():
        all_checks_passed = False
    
    # 6. Tests automatisés
    print("\n🧪 Tests automatisés:")
    if not run_tests():
        all_checks_passed = False
    
    # 7. Vérification de la configuration Railway
    print("\n🚂 Configuration Railway:")
    
    # Vérifier le contenu du Procfile
    try:
        with open("Procfile", "r") as f:
            procfile_content = f.read().strip()
            if "python start.py" in procfile_content:
                print("✅ Procfile: Configuration correcte")
            else:
                print(f"❌ Procfile: Configuration incorrecte - {procfile_content}")
                all_checks_passed = False
    except Exception as e:
        print(f"❌ Procfile: Erreur de lecture - {e}")
        all_checks_passed = False
    
    # Vérifier runtime.txt
    try:
        with open("runtime.txt", "r") as f:
            runtime_content = f.read().strip()
            if runtime_content.startswith("python-3."):
                print(f"✅ Runtime: {runtime_content}")
            else:
                print(f"❌ Runtime: Version incorrecte - {runtime_content}")
                all_checks_passed = False
    except Exception as e:
        print(f"❌ Runtime: Erreur de lecture - {e}")
        all_checks_passed = False
    
    # 8. Résumé final
    print("\n" + "=" * 50)
    if all_checks_passed:
        print("🎉 TOUTES LES VÉRIFICATIONS PASSÉES!")
        print("✅ Votre application est prête pour Railway")
        print()
        print("🚀 Prochaines étapes:")
        print("1. Générez une clé secrète: python generate_secret_key.py")
        print("2. Déployez sur Railway: python deploy_railway.py")
        print("3. Configurez les variables d'environnement")
        print("4. Testez votre application en ligne")
        return True
    else:
        print("❌ CERTAINES VÉRIFICATIONS ONT ÉCHOUÉ")
        print("🔧 Corrigez les problèmes avant de déployer")
        print()
        print("💡 Conseils:")
        print("- Vérifiez que tous les fichiers sont présents")
        print("- Installez les dépendances: pip install -r requirements.txt")
        print("- Testez localement: python start.py")
        return False

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️  Vérification annulée")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        sys.exit(1)
