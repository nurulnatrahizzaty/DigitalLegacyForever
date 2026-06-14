#!/usr/bin/env python3
import sys

sys.path.insert(0, r"c:\Users\user\Documents\LEGACY_DIGITAL_FOREVER_PROTOTYP")

from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import app, db, User
from datetime import timedelta
from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import get_malaysia_time

with app.app_context():
    print("Creating inactive test user...")

    # Delete existing if present
    existing = User.query.filter_by(username="inactive_test_user").first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        print("Deleted existing inactive user")

    # Create new inactive user
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

    print("✓ Created inactive test user")
    print(f"  Username: inactive_test_user")
    print(f"  Email: inactive_test@example.com")
    print(f"  Password: Test@12345")
    print(f"  Last active: 30 seconds ago")
    print(f"  Should appear in admin/inactive_users with period=14s")

    # Verify
    check = User.query.filter_by(username="inactive_test_user").first()
    if check:
        print(f"✓ Verified in database: {check.username} ({check.email})")
