#!/usr/bin/env python3
"""
Générateur de clé secrète pour CycleCare
"""
import secrets
import string

def generate_secret_key(length=32):
    """Génère une clé secrète sécurisée"""
    return secrets.token_urlsafe(length)

def generate_strong_password(length=16):
    """Génère un mot de passe fort"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == '__main__':
    print("🔐 Générateur de Clés Secrètes pour CycleCare")
    print("=" * 50)
    
    # Clé secrète pour Flask
    secret_key = generate_secret_key(32)
    print(f"🔑 SECRET_KEY (Flask):")
    print(f"   {secret_key}")
    print()
    
    # Clé secrète alternative
    alt_key = generate_secret_key(64)
    print(f"🔐 SECRET_KEY Alternative (plus longue):")
    print(f"   {alt_key}")
    print()
    
    # Mot de passe fort
    password = generate_strong_password(20)
    print(f"🛡️  Mot de passe fort (exemple):")
    print(f"   {password}")
    print()
    
    print("📋 Variables d'environnement pour Railway:")
    print("=" * 50)
    print(f"SECRET_KEY={secret_key}")
    print("FLASK_ENV=production")
    print("RAILWAY_ENVIRONMENT=production")
    print()
    
    print("💡 Instructions:")
    print("1. Copiez la SECRET_KEY ci-dessus")
    print("2. Ajoutez-la dans Railway → Variables d'environnement")
    print("3. Ne partagez JAMAIS cette clé publiquement!")
    print("4. Générez une nouvelle clé pour chaque déploiement")
