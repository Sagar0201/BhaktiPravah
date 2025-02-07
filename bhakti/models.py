from django.db import models
from django.utils.html import mark_safe
import base64

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class Title(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='information', default=None, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='information', default=None, null=True)
    heading = models.CharField(max_length=100, default='Bhakti Pravah')
    info = models.TextField()  
    image_data = models.BinaryField(null=True, blank=True)  # Store image as binary data

    def __str__(self):
        return f"{self.heading} - {self.title.name}"

    def image_tag(self):
        """Convert binary image data to Base64 and render it in Django Admin."""
        if self.image_data:
            return mark_safe(f'<img src="data:image/jpeg;base64,{self.get_image_base64()}" width="100"/>')
        return "No Image"

    def get_image_base64(self):
        """Convert binary image data to Base64 string."""
        if self.image_data:
            return base64.b64encode(self.image_data).decode('utf-8')
        return ""

    image_tag.short_description = "Image Preview"

    class Meta:
        ordering = ['category__category_name', 'title__name', 'heading']

class InfoList(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_information(self, information):
        """
        Add an Information object to the InfoList, maintaining the order.
        """
        last_item = self.items.order_by('-order_number').first()
        new_order = (last_item.order_number + 1) if last_item else 1
        InfoListItem.objects.create(info_list=self, information=information, order_number=new_order)

    def __str__(self):
        return self.name

class InfoListItem(models.Model):
    info_list = models.ForeignKey(InfoList, on_delete=models.CASCADE, related_name='items')
    information = models.ForeignKey(Information, on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return f"{self.info_list.name} - {self.information.heading} (Order {self.order_number})"
