from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Если категория является дочерней, устанавливаем её бренд равным бренду родительской категории
        if self.parent and not self.brand:
            self.brand = self.parent.brand
        super().save(*args, **kwargs)

    def propagate_brand_to_children(self):
        # Обновляем бренды всех дочерних категорий
        for child in self.children.all():
            child.brand = self.brand
            child.save()
            child.propagate_brand_to_children()  # Рекурсивно обновляем дочерние категории

    def save_with_brand_propagation(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.propagate_brand_to_children()


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='advertisements_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
