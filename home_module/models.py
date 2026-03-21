from django.db import models
from django.core.validators import MinValueValidator

class InfoModel(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    short_discription = models.CharField(max_length=50, verbose_name="توضیح کوتاه")
    short_about = models.CharField(max_length=255, verbose_name="درباره شما(کوتاه)")
    about = models.TextField(verbose_name="درباره شما")
    phone_number = models.CharField(verbose_name="تلفن همراه", max_length=15)
    email = models.EmailField(verbose_name="ایمیل")
    small_address = models.CharField(verbose_name="شهر", max_length=100)
    is_freelancer = models.BooleanField(verbose_name="آیا فریلنسر هستید؟", default=True)
    work_experience = models.IntegerField(verbose_name="سابقه کار", validators=[
        MinValueValidator(0, "حداقل سابقه کار ۰ میباشد")
    ])
    degree = models.CharField(max_length=100, verbose_name="درجه")

    def __str__(self):
        return f'اطلاعات شماره {self.pk}'

    class Meta:
        verbose_name = "تنظیم"
        verbose_name_plural = "تنظیمات"