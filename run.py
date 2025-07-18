#!/usr/bin/env python3
"""
Script de lancement pour l'application CycleCare
"""
import os
import sys

def main():
    """Fonction principale de lancement"""
    try:
        # Importer l'application
        from app import app, db

        # Déterminer l'environnement
        env = os.environ.get('FLASK_ENV', 'development')

        # Créer les tables si elles n'existent pas
        with app.app_context():
            db.create_all()
            print("✅ Base de données initialisée avec succès!")

        # Configuration selon l'environnement
        if env == 'production':
            host = '0.0.0.0'
            port = int(os.environ.get('PORT', 5000))
            debug = False
            print(f"🚀 Démarrage en mode PRODUCTION sur {host}:{port}")
        else:
            host = '127.0.0.1'
            port = int(os.environ.get('PORT', 8080))  # Utiliser le port 8080 par défaut
            debug = True
            print(f"🔧 Démarrage en mode DÉVELOPPEMENT sur {host}:{port}")

        print("🌸 Application CycleCare démarrée!")
        print(f"📱 Accédez à l'application sur: http://{host}:{port}")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter l'application")
        print("")
        print("🎯 Fonctionnalités disponibles :")
        print("   • Suivi du cycle menstruel avec interface 3D")
        print("   • Calcul automatique de l'ovulation")
        print("   • Calendrier interactif")
        print("   • Historique et statistiques")
        print("")

        # Lancer l'application
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=debug
        )

    except KeyboardInterrupt:
        print("\n👋 Application arrêtée par l'utilisateur")
        sys.exit(0)
    except ImportError as e:
        print(f"❌ Erreur d'importation: {e}")
        print("💡 Assurez-vous d'avoir installé les dépendances avec: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors du démarrage de l'application: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
