from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)  # Ensure category names are unique

    class Meta:
        ordering = ['category_name']  # Automatically sort by category name in ascending order

    def __str__(self):
        return self.category_name  # Return the category name as its string representation

    
class Title(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensure the title name is unique

    class Meta:
        ordering = ['name']  # Automatically sort by the name field in ascending order

    def __str__(self):
        return self.name  # String representation of the title

class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='information',default=None, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='information',default=None,null=True)  # Connect to Title model
    heading = models.CharField(max_length=100, default='Bhakti Pravah')
    info = models.TextField()  # Field to store HTML content
    image = models.ImageField(upload_to='upload/', null=True, blank=True)  # Image field

    def __str__(self):
        return f"{self.heading} - {self.title.name} "  # String representation with category name
    
    
