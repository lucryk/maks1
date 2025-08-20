# Создайте или отредактируйте Procfile
@"
web: gunicorn myproject.wsgi:application --bind 0.0.0.0:`$PORT
"@ | Out-File -FilePath Procfile -Encoding UTF8