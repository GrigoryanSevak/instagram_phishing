from django.db import models


class Users(models.Model):
    login = models.TextField(verbose_name='Логин')
    password = models.TextField(verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    
    def __str__(self):
        return self.login
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']
    