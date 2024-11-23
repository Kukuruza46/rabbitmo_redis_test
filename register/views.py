from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.core.cache import cache
from .tasks import process_registration


def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()

            # Запускаем задачу асинхронно для обработки данных пользователя
            process_registration.delay(user_profile.id)

            # Сохраняем данные в кэш
            cache.set(f'user_profile_{user_profile.id}', user_profile, timeout=60*15)

            return redirect('user_details', user_id=user_profile.id)
    else:
        form = UserProfileForm()
    return render(request, 'register/register.html', {'form': form})


def user_details(request, user_id):
    # Получаем данные из кэша
    user_profile = cache.get(f'user_profile_{user_id}')
    if not user_profile:
        user_profile = UserProfile.objects.get(id=user_id)

    return render(request, 'register/user_details.html', {'user_profile': user_profile})

def user_list(request):
    # Получаем пользователей из кэша
    users = cache.get('user_list')
    if not users:
        users = UserProfile.objects.all()
        cache.set('user_list', users, timeout=60*15)  # Кэшируем на 15 минут
    return render(request, 'register/user_list.html', {'users': users})
