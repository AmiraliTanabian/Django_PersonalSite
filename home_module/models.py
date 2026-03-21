from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class InfoModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
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
    avatar = models.ImageField(upload_to="avatar/", verbose_name="تصویر پروفایل", null=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)

    def __str__(self):
        return f'اطلاعات شماره {self.pk}'

    def full_name(self):
        return f'{self.name} {self.last_name}'
    class Meta:
        verbose_name = "تنظیم"
        verbose_name_plural = "تنظیمات"

class SkillModel(models.Model):
    skill_name = models.CharField(max_length=100, verbose_name="نام مهارت")
    proficiency_level = models.IntegerField(verbose_name="درصد تسلط", validators=[
        MinValueValidator(0, "کمترین مقدار تسلط صفر است."),
        MaxValueValidator(100, "بیشترین مقدار تسلط ۱۰۰ است")
    ])

    def __str__(self):
        return f'{self.skill_name} | {self.proficiency_level}'

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"

class CommentModels(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    group = models.CharField(max_length=100, verbose_name="شرکت / گروه")
    profile_image = models.ImageField(upload_to='comments_image', verbose_name="تصویر کاربر")
    comment_text = models.TextField(verbose_name="متن نظر")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return self.name
