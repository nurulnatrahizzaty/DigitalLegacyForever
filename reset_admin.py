from app import app, db, User

with app.app_context():
    admin = User.query.filter_by(username='admin_765').first()
    if admin:
        new_password = 'admin123!'
        admin.set_password(new_password)
        db.session.commit()
        print(f"Admin password reset to '{new_password}'")
        print("Username: admin_765")
        print("Role:", admin.role)
        print("You can now login with these credentials.")
    else:
        print("Admin not found. Run create_admin.py first.")

