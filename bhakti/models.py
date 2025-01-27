from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)  # Ensure category names are unique

    def __str__(self):
        return self.category_name  # Return the category name as its string representation

class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='information')
    info = models.TextField()  # Field to store HTML content
    image = models.ImageField(upload_to='information_images/', null=True, blank=True)  # Image field

    def __str__(self):
        return f"Information about {self.category.category_name}"  # String representation with category name
