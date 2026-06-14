from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User, EmergencyRequest

with app.app_context():
    print("=== CHECKING ADMINS ===")
    admins = User.query.filter_by(role="admin").all()
    for admin in admins:
        print(f"Admin: {admin.username} ({admin.email}) - ID: {admin.id}")

    if not admins:
        print("NO ADMINS FOUND IN DATABASE!")

    print("\n=== CHECKING EMERGENCY REQUESTS ===")
    reqs = EmergencyRequest.query.all()
    for req in reqs:
        print(f"Request ID: {req.id}")
        print(f"  From: {req.fullname} ({req.email})")
        print(f"  For account: {req.user_email}")
        print(f"  Relationship: {req.relationship}")
        print(f"  Created: {req.created_at}")
        print()

    if not reqs:
        print("NO EMERGENCY REQUESTS FOUND!")
