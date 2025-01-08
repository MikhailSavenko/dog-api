#!/bin/bash

# Ждем, пока база данных будет доступна
while !</dev/tcp/db/5432; do
  echo "База данных недоступна, ждем..."
  sleep 1
done

# Миграции
echo "Создание и приминение миграций..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Запускаем приложение
echo "Запуск приложения..."
gunicorn dog_api.wsgi --bind 0.0.0.0:8000