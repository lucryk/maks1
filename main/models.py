from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            # Логируем ошибку
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Ошибка при сохранении заявки: {str(e)}")
            raise

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'