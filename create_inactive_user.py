from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User
from datetime import timedelta
from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import get_malaysia_time

with app.app_context():
    # Create an inactive test user with last_active set to 30 seconds ago
    inactive_user = User.query.filter_by(username="inactive_test_user").first()
    if not inactive_user:
        inactive_user = User(
            username="inactive_test_user",
            email="inactive_test@example.com",
            fullname="Inactive Test User",
            role="user",
            last_active=get_malaysia_time() - timedelta(seconds=30),
        )
        inactive_user.set_password("Test@12345")
        db.session.add(inactive_user)
        db.session.commit()
        print(f"Created inactive test user with last_active 30 seconds ago")
        print(f"Username: inactive_test_user")
        print(f"Email: inactive_test@example.com")
        print(f"Password: Test@12345")
    else:
        # Update last_active to 30 seconds ago
        inactive_user.last_active = get_malaysia_time() - timedelta(seconds=30)
        db.session.commit()
        print(f"Updated existing user to be inactive (30 seconds ago)")
