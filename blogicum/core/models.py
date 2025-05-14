from django.db import models


class BaseModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        null=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
