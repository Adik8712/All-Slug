from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Категория")
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")

    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
        verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return f"{self.name} - {self.price} - {self.created_at}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"