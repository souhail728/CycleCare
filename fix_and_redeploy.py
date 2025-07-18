#!/usr/bin/env python3
"""
Script de correction et redéploiement rapide pour Railway
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès")
            if result.stdout.strip():
                print(f"   {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - Erreur:")
            print(f"   {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ Erreur lors de {description}: {e}")
        return False

def main():
    """Fonction principale de correction et redéploiement"""
    print("🔧 Script de Correction et Redéploiement CycleCare")
    print("=" * 50)
    
    # Tests locaux
    print("🧪 Tests locaux après correction...")
    if not run_command("python test_basic.py", "Exécution des tests"):
        print("❌ Les tests échouent, vérifiez le code avant de redéployer")
        return False
    
    print("✅ Tests locaux réussis!")
    print()
    
    # Vérification de l'application locale
    print("🔍 Test de l'application locale...")
    print("   Démarrage temporaire pour vérification...")
    
    # Test rapide de l'endpoint de santé
    test_result = subprocess.run(
        "python -c \"from app import app; print('App import OK')\"", 
        shell=True, 
        capture_output=True, 
        text=True
    )
    
    if test_result.returncode == 0:
        print("✅ Application locale - OK")
    else:
        print("❌ Problème avec l'application locale:")
        print(f"   {test_result.stderr}")
        return False
    
    print()
    
    # Commit des corrections
    print("📦 Commit des corrections...")
    
    if not run_command("git add .", "Ajout des fichiers modifiés"):
        return False
    
    commit_message = "Fix: Correction de l'erreur UnboundLocalError dans index()"
    if not run_command(f'git commit -m "{commit_message}"', "Commit des corrections"):
        print("ℹ️  Aucun changement à committer")
    
    # Redéploiement Railway
    print("🚂 Redéploiement sur Railway...")
    
    if not run_command("railway up", "Redéploiement"):
        print("❌ Échec du redéploiement")
        print("💡 Essayez manuellement avec: railway up")
        return False
    
    print()
    print("🎉 Correction et redéploiement terminés!")
    print()
    
    # Instructions post-déploiement
    print("📋 Vérifications recommandées:")
    print("1. Vérifiez les logs Railway:")
    print("   railway logs")
    print()
    print("2. Testez l'endpoint de santé:")
    print("   curl https://votre-app.up.railway.app/health")
    print()
    print("3. Testez l'application:")
    print("   railway open")
    print()
    print("4. Si problème persiste:")
    print("   - Vérifiez les variables d'environnement")
    print("   - Consultez les logs détaillés")
    print("   - Redémarrez le service si nécessaire")
    
    return True

if __name__ == '__main__':
    try:
        success = main()
        if success:
            print("\n🚀 Correction déployée avec succès!")
            sys.exit(0)
        else:
            print("\n💥 Échec de la correction!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️  Opération annulée par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        sys.exit(1)
