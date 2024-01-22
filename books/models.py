from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BookImageModel(models.Model):
    pass


class GenderModel(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
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
    languages = models.ForeignKey(BookLanguageModel, on_delete=models.CASCADE)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    book_cover = models.ForeignKey(BookCoverModel, on_delete=models.CASCADE)
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.OneToOneField(BookImageModel, on_delete=models.CASCADE)
    type_language = models.CharField(max_length=100)
    pages_count = models.IntegerField()
    size = models.CharField(max_length=2)  # A3, A5
    book_created = models.DateField()  # kitobni chiqan yili
    created_at = models.DateTimeField(auto_now_add=True)  # Saytdaga qoyilgan vaqti
    stars = models.FloatField()
    cash_status = models.BooleanField(default=True)  # sotuvda bor yoqligi
    readed = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    well_read = models.IntegerField(default=0)
    price = models.FloatField()  # chegrmadagi narxi
    real_price = models.FloatField()  # asl narxi
    discount = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )  # chegirma foizi 10%
