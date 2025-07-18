#!/usr/bin/env python3
"""
Script de démarrage optimisé pour Railway
"""
import os
import sys

def main():
    """Fonction principale pour Railway"""
    try:
        # Importer l'application
        from app import app, db
        
        # Configuration Railway
        port = int(os.environ.get('PORT', 8080))
        host = '0.0.0.0'
        
        # Déterminer l'environnement
        is_production = os.environ.get('RAILWAY_ENVIRONMENT') == 'production'
        debug = not is_production
        
        # Initialiser la base de données
        with app.app_context():
            db.create_all()
            print("✅ Base de données initialisée!")
        
        if is_production:
            print(f"🚂 CycleCare déployé sur Railway - Production")
        else:
            print(f"🔧 CycleCare en développement sur Railway")
        
        print(f"🌸 Application accessible sur le port {port}")
        
        # Lancer l'application
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=False  # Désactiver le reloader sur Railway
        )
        
    except Exception as e:
        print(f"❌ Erreur de démarrage: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
