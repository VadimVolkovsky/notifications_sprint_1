from celery import Celery
import os

from celery.schedules import crontab

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

# Создание экземпляра приложения Celery
app = Celery('src', broker=os.getenv('CELERY_BROKER_URL'))
# app.config_from_object('celeryconfig')

# Загрузка настроек Django в Celery
app.config_from_object('django.conf:settings', namespace="CELERY")

# Автоматическое обнаружение задач (tasks) в приложениях Django
app.autodiscover_tasks()
# app.autodiscover_tasks(['app'])

app.conf.beat_schedule = {
    'fetch-and-send-movies': {
        'task': 'app.tasks.fetch_and_send_movies',
        'schedule': crontab(minute=0, hour=18, day_of_week='fri'),  # 18:00 по пятницам
    },
}

app.conf.timezone = 'UTC'  # Укажите ваш часовой пояс, если он отличается
