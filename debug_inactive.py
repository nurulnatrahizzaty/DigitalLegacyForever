#!/usr/bin/env python3
import sys

sys.path.insert(0, r"c:\Users\user\Documents\LEGACY_DIGITAL_FOREVER_PROTOTYP")

from LEGACY_DIGITAL_FOREVER_PROTOTYP.app import (
    app,
    db,
    User,
    get_malaysia_time,
    get_timedelta,
)
from datetime import timedelta
import pytz

with app.app_context():
    print("=== DEBUGGING INACTIVE USERS QUERY ===\n")

    # Check current time
    now = get_malaysia_time()
    print(f"Current Malaysia time: {now}")
    print(f"Current Malaysia time (naive): {now.replace(tzinfo=None)}\n")

    # Get 14s timedelta
    period_delta = get_timedelta("14s")
    print(f"Period delta (14s): {period_delta}")

    # Calculate threshold
    time_ago = (now - period_delta).astimezone(pytz.utc).replace(tzinfo=None)
    print(f"Threshold (14s ago, UTC, naive): {time_ago}\n")

    # Check all users
    all_users = User.query.filter(User.role == "user").all()
    print(f"Total regular users: {len(all_users)}")
    for u in all_users:
        print(f"  - {u.username}: last_active={u.last_active}")

    print()

    # Apply the query from admin_inactive_users
    users = (
        User.query.filter(
            User.role == "user",
            db.or_(User.last_active < time_ago, User.last_active.is_(None)),
        )
        .order_by(User.created_at.desc())
        .all()
    )

    print(f"Inactive users (< {time_ago}): {len(users)}")
    for u in users:
        print(f"  - {u.username}: last_active={u.last_active}")

    # Try creating an inactive user
    print("\n=== CREATING TEST INACTIVE USER ===")
    inactive = User(
        username="test_inactive_now",
        email="test_inactive_now@example.com",
        fullname="Test Inactive Now",
        role="user",
        last_active=get_malaysia_time() - timedelta(seconds=60),
    )
    inactive.set_password("Test@12345")
    db.session.add(inactive)
    db.session.commit()
    print(f"Created: {inactive.username}")
    print(f"  last_active: {inactive.last_active}")
    print(
        f"  Should be < {time_ago}? {inactive.last_active < time_ago if inactive.last_active else 'NULL'}"
    )
