from django import forms
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Title, Information, InfoList, InfoListItem

class InformationForm(forms.ModelForm):
    image_file = forms.FileField(required=False)

    class Meta:
        model = Information
        fields = ('category', 'title', 'heading', 'info', 'image_file')

    def save(self, commit=True):
        """Convert uploaded image to binary and save it."""
        instance = super().save(commit=False)
        if self.cleaned_data.get('image_file'):
            instance.image_data = self.cleaned_data['image_file'].read()
        if commit:
            instance.save()
        return instance

class InformationAdmin(admin.ModelAdmin):
    form = InformationForm
    list_display = ('heading', 'title', 'category', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        """Render binary image as a Base64 image in Django admin."""
        if obj.image_data:
            return mark_safe(f'<img src="data:image/jpeg;base64,{obj.get_image_base64()}" width="100"/>')
        return "No Image"

    image_tag.short_description = "Image Preview"

class InfoListItemInline(admin.TabularInline):
    model = InfoListItem
    extra = 1  # Allow adding new items directly in InfoList

class InfoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    inlines = [InfoListItemInline]  # Show items in InfoList admin

admin.site.register(Category)
admin.site.register(Title)
admin.site.register(Information, InformationAdmin)
admin.site.register(InfoList, InfoListAdmin)
admin.site.register(InfoListItem)
