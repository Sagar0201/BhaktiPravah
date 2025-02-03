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
    
    


class InfoList(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Link info list to multiple Information objects
    information = models.ManyToManyField(Information, related_name='info_lists', blank=True)
    

    class Meta:
        ordering = ['-created_at']  # Newest info lists first

    def __str__(self):
        return self.name
    
    def add_information(self, information):
        """
        Add Information to InfoList and assign it the correct order based on sequence.
        """
        # Get the current highest order value in the info list or default to 0
        current_order = InfoListInformation.objects.filter(info_list=self).count()
        
        # Create a new InfoListInformation record with the next order number
        InfoListInformation.objects.create(info_list=self, information=information, order=current_order + 1)
    
    
    
class InfoListInformation(models.Model):
    info_list = models.ForeignKey(InfoList, on_delete=models.CASCADE)
    information = models.ForeignKey('Information', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()  # Order of the information in the list

    class Meta:
        unique_together = ('info_list', 'information')  # Ensure each information appears only once per info list
        ordering = ['order']  # Ensure that information is ordered by this field

    def __str__(self):
        return f"{self.info_list.name} - {self.information.heading} (Order: {self.order})"