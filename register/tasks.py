from celery import shared_task
from .models import UserProfile
from time import sleep

@shared_task
def process_registration(user_id):
    sleep(5)  # Имитация долгой обработки данных
    user = UserProfile.objects.get(id=user_id)
    print(f'Пользователь {user.name} обработан!')

    # Пример имитации отправки приветственного письма
    send_welcome_email(user)

def send_welcome_email(user):
    # Здесь мы просто симулируем отправку приветственного письма
    print(f'Приветственное письмо отправлено пользователю {user.name} на email (симуляция)')