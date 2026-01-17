# Three-page Django Site

Requirements:
- Python 3.13.4
- Django 5.1.6

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pages:
- Landing (login/logout/signup): /
- Hello: /hello/
- Goodbye: /goodbye/
