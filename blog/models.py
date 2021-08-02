from django.db import models
from login.models import CustomUser
from django.urls import reverse
from django.utils import timezone
from extensions.utils import jalali_converter


# Create your models here.
class CategoryManage(models.Manager):
    def active(self):
        return self.filter(status=True)


class Categoty(models.Model):
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='child',verbose_name='عبارت زیر دسته')
    name = models.CharField(max_length=20, verbose_name="نام")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="لینک کوتاه")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود")
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position' ]

    def __str__(self):
        return self.name




# class PostManager(models.Manager):
# def get_queryset(self):
#   return super(PostManager,self).get_queryset().filter(status="published")


class PostManage(models.Manager):
    def published(self):
        return self.filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'در حال انتظار'),
        ('published', 'منتشر شده'),
    )
    name = models.CharField(max_length=50, verbose_name="نام")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="لینک کوتاه")
    category = models.ManyToManyField(Categoty, verbose_name="دسته بندی", related_name="posts")
    image = models.ImageField(upload_to='media', verbose_name="تصویر")
    subtitle = models.CharField(max_length=800, verbose_name="توضیحات")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_post', verbose_name="نویسنده")
    body = models.TextField(verbose_name="متن اصلی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft', verbose_name="وضعیت انتشار")
    objects = PostManage()

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ('-publish',)

    def __str__(self):
        return self.name



    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.shor_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

