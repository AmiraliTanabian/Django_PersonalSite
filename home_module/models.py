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
    avatar = models.ImageField(upload_to="avatar/", verbose_name="تصویر پروفایل", null=True, blank=True)
    instagram_address = models.URLField(verbose_name="آدرس اینستاگرام (‌اختیاری)", null=True, blank=True)
    telegram_address = models.URLField(verbose_name="آدرس تلگرام (‌اختیاری)", null=True, blank=True)
    github_address = models.URLField(verbose_name="آدرس گیت ها (‌اختیاری)", null=True, blank=True)
    linkedin_address = models.URLField(verbose_name="آدرس لینکدین (‌اختیاری)", null=True, blank=True)
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


class StatsModel(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    stats = models.IntegerField(verbose_name="عدد", validators=[
        MinValueValidator(0, 'نمیتوانید مقدار کمتر از صفر وارد کنید')
    ])

    class Meta:
        verbose_name = "آمار"
        verbose_name_plural = "آمار"

    def __str__(self):
        return self.title


class EducationModel(models.Model):
    title = models.CharField(verbose_name="عنوان تحصیلات", max_length=255)
    place = models.CharField(verbose_name="محل تحصیل", max_length=255)
    short_description = models.CharField(verbose_name="توضیحات کوتاه", max_length=255)
    start_year = models.IntegerField(verbose_name="سال شروع", validators=[
        MinValueValidator(0, 'نمیتوانید مقدار کمتر از صفر وارد کنید')
    ])
    end_year = models.IntegerField(verbose_name="سال پایان (‌صقر بزنید اگر تا الان ادامه داشته)", validators=[
        MinValueValidator(0, 'نمیتوانید مقدار کمتر از صفر وارد کنید')
    ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مدرک"
        verbose_name_plural = "مدارک"

class WorkExperience(models.Model):
    title = models.CharField(verbose_name="عنوان سابقه کار", max_length=255)
    place = models.CharField(verbose_name="شرکت / گروه", max_length=255)
    short_description = models.CharField(verbose_name="توضیحات کوتاه", max_length=255)
    start_year = models.IntegerField(verbose_name="سال شروع", validators=[
        MinValueValidator(0, 'نمیتوانید مقدار کمتر از صفر وارد کنید')
    ])
    end_year = models.IntegerField(verbose_name="سال پایان (‌صقر بزنید اگر تا الان ادامه داشته)", validators=[
        MinValueValidator(0, 'نمیتوانید مقدار کمتر از صفر وارد کنید')
    ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "سابقه"
        verbose_name_plural = "سوابق"

class AttributeModel(models.Model):
    title = models.CharField(verbose_name="نام ویژگی", max_length=255)
    short_discription = models.CharField(verbose_name="توضیحی کوتاه", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

class PortfolioCategoryModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام دسته بندی نمونه کار")
    slug = models.SlugField(verbose_name="اسلاگ ( نام انگلیسی )", unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی نمونه کار"
        verbose_name_plural = "دسته بندی های نمونه کار"

class PortfolioModel(models.Model):
    category = models.ForeignKey(PortfolioCategoryModel, on_delete=models.CASCADE, verbose_name="دسته بندی")
    title = models.CharField(max_length=200, verbose_name="عنوان")
    url = models.URLField(verbose_name="آدرس", null=True)
    banner = models.ImageField(upload_to="Portofolio_banner", verbose_name="بنر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کارها"

class NewsLetterModel(models.Model):
    email = models.EmailField(verbose_name="ایمیل")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ایمیل خبرنامه"
        verbose_name_plural = "ایمیل های خبرنامه"