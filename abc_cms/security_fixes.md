# Security Fixes (Task 3.2 Supporting Notes)

---

## W1 – Hard-coded credentials

### Issue
SECRET_KEY and DB credentials were stored in settings.py.

### Fix
Moved secrets into environment variables using .env file.

### Code Location
settings.py:
- SECRET_KEY = os.getenv("SECRET_KEY")
- DATABASES config updated

.env:
- SECRET_KEY
- DB credentials

### Why this works
Prevents exposure of sensitive data in source code and aligns with secure secret management practices.

---

## W2 – Insecure configuration

### Issue
DEBUG enabled and ALLOWED_HOSTS not set.

### Fix
Set:
- DEBUG = False
- ALLOWED_HOSTS = ["yourdomain.com"]

### Code Location
settings.py

### Why this works
Prevents exposure of internal system details and protects against host header attacks.