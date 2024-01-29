from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderModel(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    ]


class AuthorModel(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10, choices=GenderModel.GENDER_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.last_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookLanguageModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book Language'
        verbose_name_plural = 'Book Languages'


class PublisherModel(models.Model):  # nashiryot
    name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Publishers'
        verbose_name_plural = 'Publishers'


class BookCoverModel(models.Model):  # Muqova
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book Coverage'
        verbose_name_plural = 'Book Coverages'


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)  # signal yoziw kk

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'


class BookModel(models.Model):
    book_name = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=50)  # wtrix codi
    main_image = models.ImageField(upload_to='main_image')
    languages = models.ForeignKey(BookLanguageModel, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE, related_name='books')
    book_cover = models.ForeignKey(BookCoverModel, on_delete=models.CASCADE, related_name='books')
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='books')
    type_language = models.CharField(max_length=100)
    pages_count = models.IntegerField()
    size = models.CharField(max_length=2)  # A3, A5
    book_created = models.DateField()  # kitobni chiqan yili
    created_at = models.DateTimeField(auto_now_add=True)  # Saytdaga qoyilgan vaqti
    stars = models.FloatField(default=0.0)
    cash_status = models.BooleanField(default=True)  # sotuvda bor yoqligi
    readed = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    well_read = models.IntegerField(default=0)
    price = models.FloatField()  # asl narxi
    real_price = models.FloatField(default=0)  # chegrmadagi narxi
    discount = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ],
        blank=True
    )  # chegirma foizi 10%

    def is_discount(self):
        return bool(self.discount)

    def __str__(self):
        return self.book_name

    class Meta:
        ordering = ['-id']


class BookImageModel(models.Model):
    book = models.ForeignKey(BookModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images')

    def __str__(self):
        return self.book.book_name
