from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(u'Test name', max_length=20)
    test_options = models.BooleanField(u'Правильный ответ', default=False)

    class Meta:
        verbose_name="Test"
        verbose_name_plural="Tests"

    def __str__(self):
        return self.title