from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Application
import logging

logger = logging.getLogger(__name__)


@csrf_protect
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        logger.info(f"Получены данные: {name}, {email}, {phone}")

        # Проверяем, что все поля заполнены
        if name and email and phone:
            try:
                # Сохраняем заявку в базу данных
                application = Application(name=name, email=email, phone=phone)
                application.save()
                logger.info(f"Заявка сохранена с ID: {application.id}")
                messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
                return redirect('index')
            except Exception as e:
                logger.error(f"Ошибка при сохранении: {str(e)}")
                messages.error(request, f'Произошла ошибка при сохранении: {str(e)}')
        else:
            logger.warning("Не все поля заполнены")
            messages.error(request, 'Пожалуйста, заполните все поля формы.')

    return render(request, 'index.html')

@csrf_protect
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Проверяем, что все поля заполнены
        if name and email and phone:
            try:
                # Сохраняем заявку в базу данных
                application = Application(name=name, email=email, phone=phone)
                application.save()
                messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
                return redirect('index')
            except Exception as e:
                messages.error(request, f'Произошла ошибка при сохранении: {str(e)}')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля формы.')

    return render(request, 'index.html')