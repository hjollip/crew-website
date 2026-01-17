# django_test1

Target versions:
- Python: 3.13.4
- Django: 5.1.6

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Notes

- There are only two pages: Landing (login/logout) and Chatbot.
- User creation is disabled in the web UI. Create users via `createsuperuser` or Django admin.
- The chatbot always replies `Say what?`.
