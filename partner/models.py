from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
KOREA = 'ko'
JAPAN = 'jp'
CHINESE = 'cn'
WESTERN = 'wst'

CATEGORIES = (
( KOREA, '한식'),
( JAPAN, '일식'),
( CHINESE, '중식'),
( WESTERN, '양식'),
)
class Partner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        verbose_name="업체이름",
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="연락처",
        )
    address =models.CharField(
        max_length=100,
        verbose_name="주소"
    )
    description = models.TextField(
        verbose_name="상세 소개"
    )
    is_active = models.BooleanField(
        default=False,
        )

    category = models.CharField(
        max_length=20,
        choices = CATEGORIES,
        default = KOREA,
        verbose_name="카테고리",
    )
    image_thumbnail = ProcessedImageField(
        upload_to = 'partner/menu',
        processors = [Thumbnail(120, 120)],
        format = 'jPEG',
        options = {'qulity' : 80},
        verbose_name = "대표이미지",
    )
    def __str__(self):
        return self.name

class Menu(models.Model):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name="메뉴 이미지",
    )
    name = models.CharField(
        max_length=50,
        verbose_name="메뉴이름",
    )
    price = models.PositiveIntegerField(
        verbose_name="메뉴가격",
    )
    def __str__(self):
        return self.name
