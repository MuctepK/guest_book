from django.db import models
DEFAULT_STATUS = 'active'
STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class Note(models.Model):
    author_name = models.CharField(max_length=70, verbose_name='Автор записи')
    author_mail = models.EmailField(max_length=80, verbose_name='Почта автора')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=50, verbose_name='Статус', default=DEFAULT_STATUS,
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.author_name
