from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)  # Ensure category names are unique

    class Meta:
        ordering = ['category_name']  # Default ordering by category_name in ascending order


    def __str__(self):
        return self.category_name  # Return the category name as its string representation

    
class Title(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensure the title name is unique

    class Meta:
        ordering = ['name']

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


    class Meta:
        ordering = ['category__category_name', 'title__name', 'heading']  # Sorting by category, title, and then heading
    
    


class InfoList(models.Model):
    name = models.CharField(max_length=200, unique=True)  # Name of the InfoList
    created_at = models.DateTimeField(auto_now_add=True)

    def add_information(self, information):
        """
        Add an Information object to the InfoList, maintaining the order.
        """
        # Get the highest order number in the list
        last_item = self.items.order_by('-order_number').first()
        new_order = (last_item.order_number + 1) if last_item else 1

        # Create and save the new InfoListItem
        InfoListItem.objects.create(info_list=self, information=information, order_number=new_order)

    def __str__(self):
        return self.name
    
    
    

class InfoListItem(models.Model):
    info_list = models.ForeignKey(InfoList, on_delete=models.CASCADE, related_name='items')
    information = models.ForeignKey('Information', on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['order_number']  # Ensure InfoListItems are retrieved in order

    def __str__(self):
        return f"{self.info_list.name} - {self.information.heading} (Order {self.order_number})"

