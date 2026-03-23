from django.db import models


class ContactUsModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    phone_number = models.CharField(max_length=14, verbose_name="تلفن همراه")
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن پیام")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    def __str__(self):
        return f' پیام از {self.name}'

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"