from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menstrual_cycle.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle simple
class CycleRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    cycle_length = db.Column(db.Integer, default=28)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

@app.route('/')
def index():
    cycles = CycleRecord.query.order_by(CycleRecord.start_date.desc()).all()
    return render_template('simple_index.html', cycles=cycles)

@app.route('/add', methods=['GET', 'POST'])
def add_cycle():
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        cycle_length = int(request.form.get('cycle_length', 28))
        
        new_cycle = CycleRecord(start_date=start_date, cycle_length=cycle_length)
        db.session.add(new_cycle)
        db.session.commit()
        
        flash('Cycle ajouté avec succès!', 'success')
        return redirect(url_for('index'))
    
    return render_template('simple_add.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Application démarrée sur http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
