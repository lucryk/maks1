import os
import sys

# Путь к вашему проекту на PythonAnywhere
path = '/home/maksimkuz/maks1'
if path not in sys.path:
    sys.path.append(path)

# Указываем Django, где находятся настройки
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# Запускаем приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()