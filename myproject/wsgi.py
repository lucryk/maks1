import os
import sys

# Добавьте путь к вашему проекту
path = '/home/maksimkuznetsov/maks1'
if path not in sys.path:
    sys.path.append(path)

# Укажите настройки Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# Импортируйте и настройте WSGI приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()