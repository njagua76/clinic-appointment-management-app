from flask_cors import CORS
from flask import Flask
from clinic_backend.extensions import db
from clinic_backend.config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object("clinic_backend.config.Config")

    db.init_app(app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    from clinic_backend.routes.patient_routes import patients_bp
    from clinic_backend.routes.doctor_routes import doctors_bp
    from clinic_backend.routes.appointment_routes import appointments_bp

    app.register_blueprint(patients_bp, url_prefix="/patients")
    app.register_blueprint(doctors_bp, url_prefix="/doctors")
    app.register_blueprint(appointments_bp, url_prefix="/appointments")

    with app.app_context():
        from clinic_backend.models import Patient, Doctor, Appointment
        db.create_all()

    return app
