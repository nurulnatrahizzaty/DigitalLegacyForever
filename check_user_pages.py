import requests
paths = ['/user/dashboard', '/user/social-connect']
for path in paths:
    try:
        r = requests.get('http://127.0.0.1:5000' + path, allow_redirects=True, timeout=10)
        print(path, 'status', r.status_code)
        print(r.text[:1200])
        print('---')
    except Exception as e:
        print(path, 'error', repr(e))
