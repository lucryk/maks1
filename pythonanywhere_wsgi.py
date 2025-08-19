import os
import sys

# Добавляем путь к проекту в системный путь
path = '/home/yourusername/yourprojectname'  # ЗАМЕНИТЕ yourusername и yourprojectname
if path not in sys.path:
    sys.path.append(path)

# Указываем настройки Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# Запускаем приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()