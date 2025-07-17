from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

# Configuration sécurisée
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///menstrual_cycle.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration de sécurité pour la production
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

db = SQLAlchemy(app)

# Modèles de données
class CycleRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    cycle_length = db.Column(db.Integer, default=28)
    period_length = db.Column(db.Integer, default=5)
    symptoms = db.Column(db.Text)
    mood = db.Column(db.String(50))
    flow_intensity = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<CycleRecord {self.start_date}>'

# Fonctions utilitaires pour les calculs
def calculate_ovulation_date(start_date, cycle_length=28):
    """Calcule la date d'ovulation (généralement 14 jours avant les prochaines règles)"""
    ovulation_day = cycle_length - 14
    return start_date + timedelta(days=ovulation_day)

def calculate_fertile_window(ovulation_date):
    """Calcule la fenêtre fertile (5 jours avant et 1 jour après l'ovulation)"""
    fertile_start = ovulation_date - timedelta(days=5)
    fertile_end = ovulation_date + timedelta(days=1)
    return fertile_start, fertile_end

def get_cycle_phase(current_date, start_date, cycle_length=28):
    """Détermine la phase actuelle du cycle"""
    days_since_start = (current_date - start_date).days

    if days_since_start < 0:
        return "Avant le cycle"
    elif days_since_start <= 5:
        return "Menstruation"
    elif days_since_start <= 13:
        return "Phase folliculaire"
    elif days_since_start <= 15:
        return "Ovulation"
    elif days_since_start <= cycle_length:
        return "Phase lutéale"
    else:
        return "Cycle suivant"

def get_average_cycle_length(user_cycles):
    """Calcule la durée moyenne des cycles d'une utilisatrice"""
    if not user_cycles or len(user_cycles) < 2:
        return 28  # Valeur par défaut

    cycle_lengths = []
    for i in range(len(user_cycles) - 1):
        current_cycle = user_cycles[i]
        next_cycle = user_cycles[i + 1]
        length = (current_cycle.start_date - next_cycle.start_date).days
        if 21 <= length <= 35:  # Cycles normaux seulement
            cycle_lengths.append(length)

    if cycle_lengths:
        return round(sum(cycle_lengths) / len(cycle_lengths))
    return 28

def predict_next_cycles(latest_cycle, num_predictions=3):
    """Prédit les prochains cycles basés sur le dernier cycle"""
    predictions = []
    current_start = latest_cycle.start_date
    cycle_length = latest_cycle.cycle_length

    for i in range(1, num_predictions + 1):
        next_start = current_start + timedelta(days=cycle_length * i)
        ovulation_date = calculate_ovulation_date(next_start, cycle_length)
        fertile_start, fertile_end = calculate_fertile_window(ovulation_date)

        predictions.append({
            'cycle_number': i,
            'start_date': next_start,
            'ovulation_date': ovulation_date,
            'fertile_start': fertile_start,
            'fertile_end': fertile_end,
            'end_date': next_start + timedelta(days=latest_cycle.period_length - 1)
        })

    return predictions

def calculate_cycle_regularity(cycles):
    """Calcule la régularité des cycles (écart-type des longueurs)"""
    if len(cycles) < 3:
        return None

    cycle_lengths = []
    for i in range(len(cycles) - 1):
        current_cycle = cycles[i]
        next_cycle = cycles[i + 1]
        length = (current_cycle.start_date - next_cycle.start_date).days
        if 21 <= length <= 35:
            cycle_lengths.append(length)

    if len(cycle_lengths) < 2:
        return None

    mean_length = sum(cycle_lengths) / len(cycle_lengths)
    variance = sum((x - mean_length) ** 2 for x in cycle_lengths) / len(cycle_lengths)
    std_dev = variance ** 0.5

    return {
        'mean': round(mean_length, 1),
        'std_dev': round(std_dev, 1),
        'regularity': 'Régulier' if std_dev <= 2 else 'Irrégulier' if std_dev <= 4 else 'Très irrégulier'
    }

# Routes
@app.route('/')
def index():
    # Récupérer les cycles de l'utilisatrice
    latest_cycle = CycleRecord.query.order_by(CycleRecord.start_date.desc()).first()
    all_cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).limit(12).all()

    current_phase = None
    next_period = None
    ovulation_date = None
    fertile_window = None
    predictions = None
    cycle_stats = None

    if latest_cycle:
        today = datetime.now().date()

        # Utiliser la durée moyenne des cycles si disponible
        avg_cycle_length = get_average_cycle_length(all_cycles)
        actual_cycle_length = avg_cycle_length if len(all_cycles) > 2 else latest_cycle.cycle_length

        current_phase = get_cycle_phase(today, latest_cycle.start_date, actual_cycle_length)

        # Calculer la prochaine période
        next_period = latest_cycle.start_date + timedelta(days=actual_cycle_length)

        # Calculer l'ovulation
        ovulation_date = calculate_ovulation_date(latest_cycle.start_date, actual_cycle_length)

        # Calculer la fenêtre fertile
        fertile_start, fertile_end = calculate_fertile_window(ovulation_date)
        fertile_window = (fertile_start, fertile_end)

        # Prédictions des prochains cycles
        predictions = predict_next_cycles(latest_cycle)

        # Statistiques des cycles
        if len(all_cycles) >= 3:
            cycle_stats = calculate_cycle_regularity(all_cycles)

    # Calculer les jours jusqu'aux événements
    days_to_next_period = None
    days_to_ovulation = None
    is_fertile_today = False

    if next_period:
        days_to_next_period = (next_period - today).days

    if ovulation_date:
        days_to_ovulation = (ovulation_date - today).days

    if fertile_window:
        is_fertile_today = fertile_window[0] <= today <= fertile_window[1]

    return render_template('index.html',
                         latest_cycle=latest_cycle,
                         current_phase=current_phase,
                         next_period=next_period,
                         ovulation_date=ovulation_date,
                         fertile_window=fertile_window,
                         predictions=predictions,
                         cycle_stats=cycle_stats,
                         days_to_next_period=days_to_next_period,
                         days_to_ovulation=days_to_ovulation,
                         is_fertile_today=is_fertile_today,
                         today=today)

@app.route('/add_cycle', methods=['GET', 'POST'])
def add_cycle():
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date = None
        if request.form.get('end_date'):
            end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
        
        cycle_length = int(request.form.get('cycle_length', 28))
        period_length = int(request.form.get('period_length', 5))
        symptoms = request.form.get('symptoms', '')
        mood = request.form.get('mood', '')
        flow_intensity = request.form.get('flow_intensity', '')
        
        new_cycle = CycleRecord(
            start_date=start_date,
            end_date=end_date,
            cycle_length=cycle_length,
            period_length=period_length,
            symptoms=symptoms,
            mood=mood,
            flow_intensity=flow_intensity
        )
        
        db.session.add(new_cycle)
        db.session.commit()
        
        flash('Cycle ajouté avec succès!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_cycle.html')

@app.route('/history')
def history():
    cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).all()
    return render_template('history.html', cycles=cycles)

@app.route('/calendar')
def calendar():
    cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).limit(12).all()
    
    calendar_data = []
    for cycle in cycles:
        ovulation_date = calculate_ovulation_date(cycle.start_date, cycle.cycle_length)
        fertile_start, fertile_end = calculate_fertile_window(ovulation_date)
        
        calendar_data.append({
            'id': cycle.id,
            'start_date': cycle.start_date.isoformat(),
            'end_date': cycle.end_date.isoformat() if cycle.end_date else None,
            'ovulation_date': ovulation_date.isoformat(),
            'fertile_start': fertile_start.isoformat(),
            'fertile_end': fertile_end.isoformat(),
            'cycle_length': cycle.cycle_length
        })
    
    return render_template('calendar.html', calendar_data=calendar_data)

@app.route('/api/cycle_data')
def api_cycle_data():
    cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).limit(12).all()

    data = []
    for cycle in cycles:
        ovulation_date = calculate_ovulation_date(cycle.start_date, cycle.cycle_length)
        fertile_start, fertile_end = calculate_fertile_window(ovulation_date)

        data.append({
            'id': cycle.id,
            'start_date': cycle.start_date.isoformat(),
            'end_date': cycle.end_date.isoformat() if cycle.end_date else None,
            'ovulation_date': ovulation_date.isoformat(),
            'fertile_start': fertile_start.isoformat(),
            'fertile_end': fertile_end.isoformat(),
            'cycle_length': cycle.cycle_length,
            'symptoms': cycle.symptoms,
            'mood': cycle.mood,
            'flow_intensity': cycle.flow_intensity
        })

    return jsonify(data)

@app.route('/api/predictions')
def api_predictions():
    """API pour obtenir les prédictions des prochains cycles"""
    latest_cycle = CycleRecord.query.order_by(CycleRecord.start_date.desc()).first()

    if not latest_cycle:
        return jsonify({'error': 'Aucun cycle enregistré'}), 404

    predictions = predict_next_cycles(latest_cycle, 6)  # 6 mois de prédictions

    # Convertir les dates en format ISO
    for prediction in predictions:
        prediction['start_date'] = prediction['start_date'].isoformat()
        prediction['ovulation_date'] = prediction['ovulation_date'].isoformat()
        prediction['fertile_start'] = prediction['fertile_start'].isoformat()
        prediction['fertile_end'] = prediction['fertile_end'].isoformat()
        prediction['end_date'] = prediction['end_date'].isoformat()

    return jsonify(predictions)

@app.route('/api/stats')
def api_stats():
    """API pour obtenir les statistiques des cycles"""
    cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).all()

    if len(cycles) < 2:
        return jsonify({'error': 'Pas assez de données pour les statistiques'}), 400

    stats = {
        'total_cycles': len(cycles),
        'average_cycle_length': get_average_cycle_length(cycles),
        'regularity': calculate_cycle_regularity(cycles)
    }

    # Statistiques des symptômes les plus fréquents
    symptoms_count = {}
    moods_count = {}
    flow_intensity_count = {}

    for cycle in cycles:
        if cycle.symptoms:
            symptoms = [s.strip().lower() for s in cycle.symptoms.split(',')]
            for symptom in symptoms:
                symptoms_count[symptom] = symptoms_count.get(symptom, 0) + 1

        if cycle.mood:
            moods_count[cycle.mood] = moods_count.get(cycle.mood, 0) + 1

        if cycle.flow_intensity:
            flow_intensity_count[cycle.flow_intensity] = flow_intensity_count.get(cycle.flow_intensity, 0) + 1

    stats['most_common_symptoms'] = sorted(symptoms_count.items(), key=lambda x: x[1], reverse=True)[:5]
    stats['mood_distribution'] = moods_count
    stats['flow_intensity_distribution'] = flow_intensity_count

    return jsonify(stats)

@app.route('/health')
def health_check():
    """Endpoint de vérification de santé pour Railway"""
    try:
        # Vérifier la base de données
        with app.app_context():
            db.session.execute('SELECT 1')

        return jsonify({
            'status': 'healthy',
            'message': 'CycleCare is running properly',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'version': '1.0.0'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'message': f'Health check failed: {str(e)}',
            'timestamp': datetime.now(timezone.utc).isoformat()
        }), 500

if __name__ == '__main__':
    import os

    # Configuration pour Railway
    port = int(os.environ.get('PORT', 8080))
    host = '0.0.0.0'  # Railway nécessite 0.0.0.0
    debug = os.environ.get('FLASK_ENV') != 'production'

    with app.app_context():
        db.create_all()
        print("✅ Base de données initialisée avec succès!")

    print(f"🚂 Démarrage de CycleCare sur Railway - Port: {port}")
    app.run(host=host, port=port, debug=debug)
