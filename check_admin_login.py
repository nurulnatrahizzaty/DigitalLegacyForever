from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, User

with app.app_context():
    admin = User.query.filter_by(username="admin_765").first()
    print("exists", bool(admin))
    if admin:
        print("email", admin.email)
        print("hash", admin.password_hash[:60] if admin.password_hash else "None")
        print("check", admin.check_password("Admin@12345"))
