from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"




class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    title = models.CharField(max_length=50, verbose_name="تیتر")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(verbose_name="تصویر")
    publish = models.DateField(verbose_name="تاریخ انتشار")
    update = models.DateField(verbose_name="آپدیت")


    def __str__(self):
        return f"{self.title} - {self.author}"
    

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="کاربر")
    text = models.TextField(verbose_name="متن")
    date = models.DateField(verbose_name="تاریخ")
    

    def __str__(self):
        return f"{self.user} - {self.article}"
    

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"




class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="کاربر")
    count = models.IntegerField(verbose_name="تعداد")
    date = models.DateTimeField(verbose_name="تاریخ")


    def __str__(self):
        return f"{self.user} - {self.article}"
    

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"

    








