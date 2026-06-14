#!/usr/bin/env python3
import sys

sys.path.insert(0, r"c:\Users\user\Documents\LEGACY_DIGITAL_FOREVER_PROTOTYP")

from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User, get_malaysia_time
from datetime import timedelta

with app.app_context():
    print("=== CREATING INACTIVE TEST USER ===\n")

    # Delete if exists
    existing = User.query.filter_by(username="test_inactive").first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        print("✓ Deleted existing test user\n")

    # Create user with last_active = 20 seconds ago
    # This ensures they appear inactive for "14 Seconds" period
    twenty_seconds_ago = get_malaysia_time() - timedelta(seconds=20)

    test_user = User(
        username="test_inactive",
        email="test_inactive@example.com",
        fullname="Test Inactive User",
        role="user",
        last_active=twenty_seconds_ago,
    )
    test_user.set_password("Test@12345")
    db.session.add(test_user)
    db.session.commit()

    print("✓ CREATED INACTIVE USER")
    print(f"  Username: test_inactive")
    print(f"  Email: test_inactive@example.com")
    print(f"  Password: Test@12345")
    print(f"  Last active: 20 seconds ago")
    print(f"\n✓ RESULT:")
    print(f"  This user will appear INACTIVE when you select '14 Seconds'")
    print(f"  in the Admin > Inactive Users page")
    print(f"\nNow go to: http://127.0.0.1:5000/admin/inactive_users")
    print(f"Select: '14 Seconds' from dropdown")
    print(f"And the user 'test_inactive' should appear!\n")
