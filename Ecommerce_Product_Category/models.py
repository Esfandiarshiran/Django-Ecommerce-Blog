from django.db import models


# class CategoryManager(models.Manager):
#     def get_category(self):
#         return self.get_queryset().first()


class ProductsCategory(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
