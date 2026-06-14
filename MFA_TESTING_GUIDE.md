# MFA Implementation Testing Guide

## ✅ Quick Start Testing

### Prerequisites

1. Email configuration in `.env` is correct
2. Application is running (port 5000)
3. Database migrations have been run

### Test Scenario 1: Successful MFA Login

**Steps**:

1. Navigate to `http://localhost:5000/login`
2. Enter username: `test_user` (or any valid user)
3. Enter password: (valid password)
4. Click "Sign In"

**Expected Result**:

- ✅ Flash message: "A verification code has been sent to your email"
- ✅ Redirect to `/verify-mfa` page
- ✅ Email received with 6-digit code
- ✅ Page shows user's email (masked partially)

**Verification**: 5. Check email inbox for code (e.g., "123456") 6. Enter code in the verification form 7. Click "Verify & Continue"

**Expected Result**:

- ✅ Flash message: "Login successful! Welcome back."
- ✅ Redirect to appropriate dashboard (admin or user)
- ✅ User is logged in

### Test Scenario 2: Expired MFA Code

**Steps**:

1. Login and get to `/verify-mfa` page
2. Wait more than 10 minutes
3. Enter code in verification form
4. Click "Verify & Continue"

**Expected Result**:

- ✅ Flash message: "MFA code has expired. Please log in again."
- ✅ Redirect back to login page

### Test Scenario 3: Invalid MFA Code

**Steps**:

1. Login and get to `/verify-mfa` page
2. Enter incorrect code (e.g., "000000")
3. Click "Verify & Continue"

**Expected Result**:

- ✅ Flash message: "Invalid verification code. 4 attempts remaining."
- ✅ Remain on verification page
- ✅ Attempt counter decrements

**Repeat 5 times**: 4. Keep entering wrong codes 5. After 5th wrong attempt, verify message: "Too many failed verification attempts. Please log in again." 6. Redirect to login page

### Test Scenario 4: No Session (Direct Access)

**Steps**:

1. Directly navigate to `http://localhost:5000/verify-mfa` without logging in
2. (No login session)

**Expected Result**:

- ✅ Flash message: "No pending MFA verification. Please log in first."
- ✅ Redirect to login page

### Test Scenario 5: Failed Login (No MFA)

**Steps**:

1. Navigate to `http://localhost:5000/login`
2. Enter username: `test_user`
3. Enter password: (wrong password)
4. Click "Sign In"

**Expected Result**:

- ✅ Flash message: "Your Username or Password wrong! Please try again. (2 attempts remaining)"
- ✅ Remain on login page
- ✅ NO email sent, NO MFA verification

## 🔍 Verification Checks

### Email Content Verification

Check the received email contains:

- ✅ Subject: "ForeverSafe - Your Login Verification Code"
- ✅ Body has 6-digit code
- ✅ Code in prominent box/section
- ✅ Expiry message: "This code will expire in 10 minutes"
- ✅ Security warning: "Do NOT share this code with anyone"
- ✅ ForeverSafe branding

### Database Verification

Run these SQL queries to verify:

```sql
-- Check MFA columns exist
PRAGMA table_info(user);

-- Check a user has MFA code stored (after login but before verification)
SELECT id, username, mfa_code, mfa_code_expiry FROM user LIMIT 1;

-- After successful verification, code should be NULL
SELECT id, username, mfa_code, mfa_code_expiry FROM user WHERE username='test_user';
```

Expected results:

- ✅ Columns: mfa_code, mfa_code_expiry, mfa_enabled exist
- ✅ After login: mfa_code is set, mfa_code_expiry is set to future time
- ✅ After verification: Both fields are NULL

### Session Verification

Check browser developer tools:

1. Open Developer Tools (F12)
2. Go to "Storage" or "Application" tab
3. Check cookies:
   - ✅ `session` cookie exists after login attempt
   - ✅ Session data contains: `mfa_pending_user_id`, `mfa_remember`, `mfa_attempts`
   - ✅ Session cleared after successful MFA verification

### Log Verification

Check Flask logs for:

```
[LOGIN SECURITY] User login initiated
[MFA EMAIL] Email sent to user@example.com
[MFA VERIFY] Code verified successfully
[LOGIN ACTION] Username logged in successfully with MFA
```

## 📊 Test Results Template

Create a test report:

```
Date: ____/__/____
Tester: ________________
Environment: [ ] Local [ ] Dev [ ] Staging [ ] Production

Test Scenario 1 - Successful MFA Login
  [ ] Pass  [ ] Fail  Notes: _______________________

Test Scenario 2 - Expired MFA Code
  [ ] Pass  [ ] Fail  Notes: _______________________

Test Scenario 3 - Invalid MFA Code (5 attempts)
  [ ] Pass  [ ] Fail  Notes: _______________________

Test Scenario 4 - Direct Access Without Session
  [ ] Pass  [ ] Fail  Notes: _______________________

Test Scenario 5 - Failed Login (No MFA Sent)
  [ ] Pass  [ ] Fail  Notes: _______________________

Email Delivery
  [ ] Email received  [ ] Code correct  [ ] Formatting OK

Database State
  [ ] Columns exist  [ ] Data stored  [ ] Data cleared after

Browser Session
  [ ] Session created  [ ] Session valid  [ ] Session cleared

Overall Status: [ ] PASS [ ] FAIL

Issues Found:
- ________________________
- ________________________
- ________________________

Recommendations:
- ________________________
- ________________________
```

## 🐛 Common Issues & Solutions

### Issue: "Email not sent" / Flash message not showing

**Solution**:

- Check MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD in .env
- Verify SMTP configuration is correct
- Check email logs for errors
- Try sending a test email

### Issue: Code expires immediately

**Solution**:

- Check server time is correct
- Verify `get_malaysia_time()` function returns correct timezone
- Sync server clock

### Issue: MFA page shows "Expired" immediately after login

**Solution**:

- Check server clock synchronization
- Verify 10-minute expiry calculation
- Check database timestamp format

### Issue: Code not matching even though correct

**Solution**:

- Check for whitespace in form input
- Verify code is stored correctly in database
- Check for case sensitivity (codes are numeric, shouldn't matter)

### Issue: Rate limiting too aggressive

**Solution**:

- Current limit: 5 attempts per MFA verification
- Current timeout: 10 minutes for code expiry
- Adjust in verify_mfa() function if needed

## 📝 Manual Testing Commands

Test via curl/terminal:

```bash
# 1. Login
curl -X POST http://localhost:5000/login \
  -d "username=test_user&password=password" \
  -c cookies.txt

# 2. Check MFA page
curl -X GET http://localhost:5000/verify-mfa \
  -b cookies.txt

# 3. Verify code
curl -X POST http://localhost:5000/verify-mfa \
  -d "mfa_code=123456" \
  -b cookies.txt
```

## ✅ Sign-Off

All tests passed? Then MFA implementation is complete and ready for:

- [ ] User acceptance testing
- [ ] Security audit
- [ ] Production deployment
- [ ] User documentation

---

**Implementation Date**: June 10, 2026
**Status**: Ready for Testing ✅
