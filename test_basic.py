#!/usr/bin/env python3
"""
Tests de base pour l'application CycleCare
"""
import unittest
import tempfile
import os
from datetime import datetime, date
from app import app, db, CycleRecord

class CycleCareTestCase(unittest.TestCase):
    """Tests de base pour CycleCare"""
    
    def setUp(self):
        """Configuration avant chaque test"""
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE']
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
    
    def test_index_page(self):
        """Test de la page d'accueil"""
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'CycleCare', rv.data)
    
    def test_add_cycle_page(self):
        """Test de la page d'ajout de cycle"""
        rv = self.app.get('/add_cycle')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Ajouter un Nouveau Cycle', rv.data)
    
    def test_add_cycle_post(self):
        """Test d'ajout d'un cycle"""
        rv = self.app.post('/add_cycle', data={
            'start_date': '2024-01-01',
            'cycle_length': '28',
            'period_length': '5',
            'mood': 'Bonne',
            'symptoms': 'Test symptômes'
        }, follow_redirects=True)
        
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'ajout', rv.data)
    
    def test_calendar_page(self):
        """Test de la page calendrier"""
        rv = self.app.get('/calendar')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Calendrier', rv.data)
    
    def test_history_page(self):
        """Test de la page historique"""
        rv = self.app.get('/history')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Historique', rv.data)
    
    def test_api_cycle_data(self):
        """Test de l'API des données de cycle"""
        rv = self.app.get('/api/cycle_data')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.content_type, 'application/json')
    
    def test_cycle_model(self):
        """Test du modèle CycleRecord"""
        with app.app_context():
            # Créer un cycle de test
            cycle = CycleRecord(
                start_date=date(2024, 1, 1),
                cycle_length=28,
                period_length=5,
                mood='Bonne',
                symptoms='Test'
            )
            
            db.session.add(cycle)
            db.session.commit()
            
            # Vérifier que le cycle a été créé
            saved_cycle = CycleRecord.query.first()
            self.assertIsNotNone(saved_cycle)
            self.assertEqual(saved_cycle.cycle_length, 28)
            self.assertEqual(saved_cycle.mood, 'Bonne')

def run_tests():
    """Exécuter tous les tests"""
    print("🧪 Lancement des tests CycleCare...")
    
    # Créer une suite de tests
    suite = unittest.TestLoader().loadTestsFromTestCase(CycleCareTestCase)
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Afficher les résultats
    if result.wasSuccessful():
        print("✅ Tous les tests sont passés avec succès!")
        return True
    else:
        print("❌ Certains tests ont échoué.")
        return False

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
