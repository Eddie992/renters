release: cd rentershub && python manage.py makemigrations users listings && python manage.py migrate
web: cd rentershub && gunicorn rentershub.wsgi:application --bind 0.0.0.0:$PORT
