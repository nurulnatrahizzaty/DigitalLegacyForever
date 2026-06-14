from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User.query.filter_by(username="admin_765").first()
    if admin:
        print(f"Admin found: {admin.username}")
        # Use werkzeug hash directly - this will work with check_password logic
        admin.password_hash = generate_password_hash(
            "Admin@12345", method="pbkdf2:sha256"
        )
        db.session.commit()
        print(f"Password reset with werkzeug hash")
        print(f'Check result: {admin.check_password("Admin@12345")}')
    else:
        print("Admin not found")
