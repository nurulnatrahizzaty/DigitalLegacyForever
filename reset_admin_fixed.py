import sys
sys.path.insert(0, 'LEGACY_DIGITAL_FOREVER_PROTOTYP')
from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User

with app.app_context():
    admin = User.query.filter_by(username='admin_765').first()
    if admin:
        new_password = 'admin123!'
        admin.set_password(new_password)
        db.session.commit()
        print(f"Admin password reset to '{new_password}'")
        print("Username: admin_765")
        print("Role:", admin.role)
        print("Email:", admin.email)
        print("Login now at http://127.0.0.1:5000/login")
    else:
        print("Admin not found. Run create_admin.py first.")
